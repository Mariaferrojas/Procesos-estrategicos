import csv
import os

RUTA = "src/data/iniciativas.csv"

def cargar_iniciativas():
    iniciativas = []

    if not os.path.exists(RUTA):
        print(f"❌ No se encontró el archivo: {RUTA}")
        return iniciativas

    try:
        with open(RUTA, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                iniciativas.append(row)
    except Exception as e:
        print(f"Error al leer el CSV: {e}")

    return iniciativas