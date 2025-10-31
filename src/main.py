import csv
import os
from datetime import datetime


class Iniciativa:
    def __init__(self, nombre, impacto, esfuerzo, costo):
        self.nombre = nombre
        self.impacto = float(impacto)
        self.esfuerzo = float(esfuerzo)
        self.costo = float(costo)
        self.puntaje = self.calcular_puntaje()
    
    def calcular_puntaje(self):
        return self.impacto*2 - self.esfuerzo - self.costo

def cargar_iniciativas(ruta_csv):
    if not os.path.exists(ruta_csv):
        print(f"❌ No se encontró el archivo: {ruta_csv}")
        return []
    iniciativas = []
    with open(ruta_csv, newline='', encoding='utf-8-sig') as f:
        lector = csv.DictReader(f)
        for fila in lector:
            try:
                ini = Iniciativa(fila['nombre'], fila['impacto'], fila['esfuerzo'], fila['costo'])
                iniciativas.append(ini)
            except Exception as e:
                print(f" Fila inválida ignorada: {fila} -> {e}")
    return iniciativas

def generar_csv_iniciativas(iniciativas, ruta_salida):
    os.makedirs(os.path.dirname(ruta_salida), exist_ok=True)
    with open(ruta_salida, 'w', newline='', encoding='utf-8') as f:
        campos = ['nombre', 'impacto', 'esfuerzo', 'costo', 'puntaje']
        escritor = csv.DictWriter(f, fieldnames=campos)
        escritor.writeheader()
        for ini in iniciativas:
            escritor.writerow({
                'nombre': ini.nombre,
                'impacto': ini.impacto,
                'esfuerzo': ini.esfuerzo,
                'costo': ini.costo,
                'puntaje': ini.puntaje
            })

def generar_csv_metricas(iniciativas, ruta_salida):
    total = len(iniciativas)
    if total == 0:
        return
    promedio_impacto = sum(i.impacto for i in iniciativas)/total
    promedio_esfuerzo = sum(i.esfuerzo for i in iniciativas)/total
    promedio_costo = sum(i.costo for i in iniciativas)/total
    os.makedirs(os.path.dirname(ruta_salida), exist_ok=True)
    with open(ruta_salida, 'w', newline='', encoding='utf-8') as f:
        escritor = csv.writer(f)
        escritor.writerow(['Total iniciativas', 'Promedio impacto', 'Promedio esfuerzo', 'Promedio costo'])
        escritor.writerow([total, f"{promedio_impacto:.2f}", f"{promedio_esfuerzo:.2f}", f"{promedio_costo:.2f}"])

def registrar_bitacora(ruta_bitacora, total, top3):
    os.makedirs(os.path.dirname(ruta_bitacora), exist_ok=True)
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(ruta_bitacora, 'a', newline='', encoding='utf-8') as f:
        escritor = csv.writer(f)
        escritor.writerow([fecha, total, ', '.join([i.nombre for i in top3])])

def mostrar_resumen(iniciativas):
    if not iniciativas:
        print("No hay iniciativas para mostrar.")
        return
    total = len(iniciativas)
    promedio_impacto = sum(i.impacto for i in iniciativas)/total
    promedio_esfuerzo = sum(i.esfuerzo for i in iniciativas)/total
    promedio_costo = sum(i.costo for i in iniciativas)/total
    print("\n=== Resumen de Iniciativas ===")
    print(f"Total de iniciativas: {total}")
    print(f"Promedio impacto: {promedio_impacto:.2f}")
    print(f"Promedio esfuerzo: {promedio_esfuerzo:.2f}")
    print(f"Promedio costo: {promedio_costo:.2f}")
    print("Top 3 iniciativas por puntaje:")
    for i in sorted(iniciativas, key=lambda x: x.puntaje, reverse=True)[:3]:
        print(f"- {i.nombre} | Puntaje: {i.puntaje}")


def main():
    print("=== Priorizador de Iniciativas Estratégicas  ===")
    ruta_entrada = "src/data/iniciativas.csv"
    ruta_reporte = "src/data/reporte.csv"
    ruta_top = "src/data/top_iniciativas.csv"
    ruta_metricas = "src/data/metricas.csv"
    ruta_bitacora = "src/data/bitacora.csv"

    iniciativas = cargar_iniciativas(ruta_entrada)
    if not iniciativas:
        print("❌ No se pudieron cargar iniciativas. Fin del programa.")
        return

    
    iniciativas_ordenadas = sorted(iniciativas, key=lambda x: x.puntaje, reverse=True)
    top3 = iniciativas_ordenadas[:3]

    generar_csv_iniciativas(iniciativas_ordenadas, ruta_reporte)
    print(f"✅ Reporte completo generado: {ruta_reporte}")


    generar_csv_iniciativas(top3, ruta_top)
    print(f"✅ Top 3 iniciativas generado: {ruta_top}")

    
    generar_csv_metricas(iniciativas_ordenadas, ruta_metricas)
    print(f"✅ Métricas generadas: {ruta_metricas}")

    
    registrar_bitacora(ruta_bitacora, len(iniciativas_ordenadas), top3)
    print(f"✅ Bitácora actualizada: {ruta_bitacora}")

    
    mostrar_resumen(iniciativas_ordenadas)
    print("✅ Proceso finalizado.")

if __name__ == "__main__":
    main()
