def calcular_puntaje(impacto, esfuerzo, costo):

    try:
        return round(impacto / (esfuerzo + costo), 3)
    except ZeroDivisionError:
        return 0.0
    except Exception:
        return 0.0

def priorizar(iniciativas):
    
    iniciativas_validas = []

    for ini in iniciativas:
        try:
            impacto = float(ini["impacto"])
            esfuerzo = float(ini["esfuerzo"])
            costo = float(ini["costo"])
        except (KeyError, ValueError, TypeError):
            continue

        if impacto <= 0 or esfuerzo <= 0 or costo <= 0:
            continue

        ini["puntaje"] = calcular_puntaje(impacto, esfuerzo, costo)
        iniciativas_validas.append(ini)

    iniciativas_validas.sort(key=lambda x: x["puntaje"], reverse=True)
    return iniciativas_validas

def desempatar(iniciativas):
    
    iniciativas.sort(key=lambda x: (x["puntaje"], x["impacto"]), reverse=True)
    return iniciativas



def priorizar(iniciativas):
    iniciativas_validas = []

    for ini in iniciativas:
        try:
            impacto = float(ini["impacto"])
            esfuerzo = float(ini["esfuerzo"])
            costo = float(ini["costo"])
        except (KeyError, ValueError, TypeError):
            continue

        if impacto <= 0 or esfuerzo <= 0 or costo <= 0:
            continue

        ini["puntaje"] = calcular_puntaje(impacto, esfuerzo, costo)
        iniciativas_validas.append(ini)

    iniciativas_validas.sort(key=lambda x: x["puntaje"], reverse=True)
    return desempatar(iniciativas_validas)