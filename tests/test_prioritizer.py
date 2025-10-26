
import os
import sys
import math


ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from modules.prioritizer import priorizar

def almost_equal(a, b, tol=1e-9):
    return abs(a - b) <= tol

def test_prioritizer_basic_order_and_scores():
    """
    Verifica que:
    - Se calcule el puntaje esperado (impacto / (esfuerzo + costo))
    - Se ordene de mayor a menor por 'puntaje'
    - Los puntajes estén redondeados a 2 decimales
    """
    entradas = [
        {"nombre": "A", "impacto": "10", "esfuerzo": "2", "costo": "1"},
        {"nombre": "B", "impacto": "5",  "esfuerzo": "1", "costo": "1"},
        {"nombre": "C", "impacto": "8",  "esfuerzo": "4", "costo": "2"}
    ]

    resultado = priorizar(entradas)

   
    assert len(resultado) == 3

    esperado_A = round(10 / (2 + 1), 2)  
    esperado_B = round(5  / (1 + 1), 2) 
    esperado_C = round(8  / (4 + 2), 2)  

    
    puntajes = {item["nombre"]: item["puntaje"] for item in resultado}
    assert almost_equal(puntajes["A"], esperado_A)
    assert almost_equal(puntajes["B"], esperado_B)
    assert almost_equal(puntajes["C"], esperado_C)


    nombres_ordenados = [item["nombre"] for item in resultado]
    assert nombres_ordenados == ["A", "B", "C"]

def test_prioritizer_with_numeric_inputs_and_rounding():
    """
    Verifica que la función acepte valores numéricos (no solo strings)
    y que el redondeo a 2 decimales se aplique correctamente.
    """
    entradas = [
        {"nombre": "X", "impacto": 7, "esfuerzo": 3, "costo": 2.5},
        {"nombre": "Y", "impacto": 7, "esfuerzo": 2, "costo": 3.0}
    ]

    resultado = priorizar(entradas)

    assert len(resultado) == 2

    esperado_X = round(7 / (3 + 2.5), 2)
    esperado_Y = round(7 / (2 + 3.0), 2)


    mapa = {item["nombre"]: item["puntaje"] for item in resultado}
    assert almost_equal(mapa["X"], esperado_X)
    assert almost_equal(mapa["Y"], esperado_Y)

def test_prioritizer_empty_list_returns_empty():
    """Verifica que una lista vacía devuelva una lista vacía."""
    resultado = priorizar([])
    assert resultado == []
