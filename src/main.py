from modules.data_loader import cargar_iniciativas
from modules.validator import validar_iniciativas
from modules.prioritizer import priorizar
from modules.csv_report import generar_reporte

def main():
    print("=== Priorizador de Iniciativas Estratégicas ===")

    iniciativas = cargar_iniciativas()

    iniciativas_validas = validar_iniciativas(iniciativas)

    iniciativas_priorizadas = priorizar(iniciativas_validas)

    generar_reporte(iniciativas_priorizadas)

    print(" Proceso finalizado. Consulte reporte.csv")

if __name__ == "__main__":
    main()
