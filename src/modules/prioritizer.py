"""
📌 Módulo: Prioritizer
Función: Calcular y ordenar la prioridad de iniciativas estratégicas.
"""

def calcular_puntaje(impacto, esfuerzo, costo):
    """
    Calcula un puntaje basado en la relación entre impacto, esfuerzo y costo.
    Retorna un número redondeado a 3 decimales.
    """
    try:
        return round(impacto / (esfuerzo + costo), 3)
    except ZeroDivisionError:
        print("⚠️ Error: División por cero detectada. Puntaje asignado = 0.0")
        return 0.0
    except Exception as e:
        print(f"⚠️ Error inesperado al calcular puntaje: {e}")
        return 0.0


def desempatar(iniciativas):
    """
    En caso de empate, prioriza por mayor impacto.
    """
    iniciativas.sort(key=lambda x: (x["puntaje"], x["impacto"]), reverse=True)
    return iniciativas


def priorizar(iniciativas):
    """
    Valida, calcula puntajes, ordena y muestra resultados.
    """
    iniciativas_validas = []

    for ini in iniciativas:
        try:
            impacto = float(ini["impacto"])
            esfuerzo = float(ini["esfuerzo"])
            costo = float(ini["costo"])
        except (KeyError, ValueError, TypeError):
            print(f"❌ Iniciativa inválida descartada: {ini}")
            continue

        if impacto <= 0 or esfuerzo <= 0 or costo <= 0:
            print(f"⚠️ Valores no válidos en: {ini.get('nombre', 'Desconocido')}")
            continue

        ini["puntaje"] = calcular_puntaje(impacto, esfuerzo, costo)
        iniciativas_validas.append(ini)

    resultado_final = desempatar(iniciativas_validas)
    resultado_final.sort(key=lambda x: x["puntaje"], reverse=True)

    # 🔹 Mostrar todos los resultados
    print("\n🔹 RESULTADO DE PRIORIZACIÓN 🔹")
    for i, ini in enumerate(resultado_final, 1):
        print(f"{i}. {ini['nombre']} | Puntaje: {ini['puntaje']} | Impacto: {ini['impacto']} | Esfuerzo: {ini['esfuerzo']} | Costo: {ini['costo']}")

    # 🏆 Mostrar el Top 3 por puntaje
    print("\n🏆 Top 3 iniciativas por puntaje:")
    top_3 = resultado_final[:3]  # Toma las tres primeras
    for ini in top_3:
        print(f"- {ini['nombre']} | Puntaje: {ini['puntaje']}")

    print("\n✅ Prioritizer ejecutado correctamente por Andrey Llanos.")
    return resultado_final
