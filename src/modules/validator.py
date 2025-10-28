def validar_iniciativas(iniciativas):
    iniciativas_validas = []
    for ini in iniciativas:
        try:
            impacto = int(ini["impacto"])
            esfuerzo = int(ini["esfuerzo"])
            costo = float(ini["costo"])

            if impacto >= 0 and esfuerzo > 0 and costo > 0:
                iniciativas_validas.append(ini)

        except ValueError:
            print(f"❌ Datos inválidos descartados: {ini}")

    return iniciativas_validas