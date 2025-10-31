import csv

RUTA_SALIDA = "src/data/reporte.csv"

def generar_reporte(iniciativas):
    campos = ["nombre", "impacto", "esfuerzo", "costo", "puntaje"]

    try:
        with open(RUTA_SALIDA, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=campos)
            writer.writeheader()
            writer.writerows(iniciativas)

        print(f"✅ Reporte generado: {RUTA_SALIDA}")

    except Exception as e:
        print(f"❌ Error al generar el reporte: {e}")