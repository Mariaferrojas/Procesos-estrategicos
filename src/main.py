from modules.data_loader import cargar_iniciativas
from modules.validator import validar_iniciativas
from modules.prioritizer import priorizar
from modules.csv_report import generar_reporte

if __name__ == "__main__":
    print("=== Priorizador de Iniciativas Estratégicas ===")

    # 1️⃣ Cargar iniciativas desde CSV
    iniciativas = cargar_iniciativas()
    print(f"📥 Iniciativas cargadas: {len(iniciativas)}")

    # 2️⃣ Validar iniciativas
    iniciativas_validadas = validar_iniciativas(iniciativas)
    print(f"✅ Iniciativas válidas: {len(iniciativas_validadas)}")

    # 3️⃣ Calcular prioridad
    iniciativas_priorizadas = priorizar(iniciativas_validadas)

    # 4️⃣ Generar reporte CSV final
    generar_reporte(iniciativas_priorizadas)

    print("🚀 Proceso completado con éxito.")
