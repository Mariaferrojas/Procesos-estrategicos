# Procesos-estrategicos
# Priorizador de Iniciativas Estratégicas  
**Categoría:** Procesos Estratégicos  


---

## 📌 Integrantes del Equipo

- **María Fernanda Rojas** (Líder técnica)
- *[Nombre del compañero]*
- *[Nombre del compañero]*
- *[Nombre del compañero]*

---

## 🎯 Problema / Necesidad

Las organizaciones deben seleccionar adecuadamente cuáles iniciativas estratégicas ejecutar primero para asegurar el máximo impacto con el menor uso de recursos. Sin embargo, la priorización muchas veces se realiza de manera subjetiva y sin criterios claros.

Esto puede generar:
- Pérdida de recursos
- Retrasos en objetivos estratégicos
- Baja alineación con la estrategia institucional

---

## ✅ Solución Propuesta

Se desarrolló un **software en Python** que:

1. **Lee** un archivo CSV con iniciativas y sus métricas.
2. **Valida** los datos y descarta entradas incorrectas.
3. **Calcula** una puntuación de prioridad usando una fórmula basada en impacto, esfuerzo y costo.
4. **Ordena** las iniciativas de más prioritarias a menos prioritarias.
5. **Genera un nuevo archivo CSV** como reporte consolidado.
6. Muestra un resumen de resultados en consola.

En el cual no se utilizo pandas

---

## 🧩 Arquitectura del Proyecto

/ PROCESOS-ESTRATEGICOS
├─ src/
│ ├─ main.py
│ ├─ modules/
│ │ ├─ data_loader.py
│ │ ├─ validator.py
│ │ ├─ prioritizer.py
│ │ └─ csv_report.py
│ └─ data/
│ ├─ iniciativas.csv
│ └─ reporte.csv (se genera automáticamente)
├─ tests/ 
├─ requirements.txt
├─ README.md
└─ .gitignore


---

##  Temas de Python aplicados

- Funciones
- Módulos e importaciones
- Programación basada en archivos (CSV)
- Estructuras de datos (listas y diccionarios)
- Manejo de excepciones
- Ordenamiento y procesamiento de datos
- POO básica (si se agregan mejoras futuras)

---

## 🛠 Requisitos Técnicos

- **Python 3.13.** 
- Sistema operativo: Windows
- Entorno virtual 

---

## ▶️ Manual de Usuario

### 1 Crear entorno virtual (NO subirlo al repositorio)

```sh
python -m venv venv
