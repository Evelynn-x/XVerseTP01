#  PROYECTO XVERSE

## 📌 Descripción
Este proyecto forma parte de los trabajos prácticos de programación (TP01, TP02 y TP03).  
El objetivo es practicar y aplicar:
- Lectura y manejo de archivos JSON en Python.
- Uso de estructuras de datos (listas, búsqueda secuencial, árbol binario).
- Comparación de eficiencia entre distintos métodos de búsqueda.
- Presentación de resultados en consola con formato claro.
- Experimentos de rendimiento con datasets de distinto tamaño.

El programa carga un dataset de videojuegos (`videojuegos.json`) y permite:
- Listar títulos con sus datos.
- Buscar y filtrar por distintos criterios.
- Comparar búsqueda secuencial vs. búsqueda con árbol binario.
- Ejecutar pruebas de rendimiento con datasets de 100, 1000 y 10000 juegos.

---

## 👥 Integrantes
- Ariana Evelyn Nicole Ortiz Pereira  
- Lautaro Auer  
- Thiago Gabriel Esquivel  

---

##  Ejecución del proyecto
Para correr cada trabajo práctico desde la terminal, ubicándote en la carpeta principal del repositorio:

```bash
# TP01 – Versión inicial
# Script principal con menú básico y búsqueda secuencial
py TP01/XVERSE_TP_01.py

# TP02 – Experimentos de búsqueda
# Comparación de cuatro métodos de búsqueda utilizando datasets de distinto tamaño
py TP02/experimentos.py

# TP03 – Versión extendida
# Aplicación con menú interactivo y búsqueda mediante árbol binario
py TP03/XVERSE_TP_03.py

# TP03 – Experimentos de rendimiento
# Pruebas comparativas de eficiencia entre búsqueda secuencial y árbol binario
py TP03/experimentos_tp03.py

---
---

PROYECTO XVERSE/
├── TP01/
│   └── XVERSE_TP_01.py
│   
├── TP02/
│   ├── experimentos.py
│   ├── generar_dataset.py
│   ├── juegos_100.json
│   ├── juegos_1000.json
│   └── juegos_10000.json
│  
│
├── TP03/
│   ├── XVERSE_TP_03.py
│   ├── experimentos_tp03.py
│   ├── juegos_100.json
│   ├── juegos_1000.json
│   └── juegos_10000.json
│   
│
├── docs/
│   ├── capturas/
│   │   ├── diagrama-clases.drawio
│   │   ├── diagrama-clases.png
│   │   ├── diagrama-datos.drawio
│   │   └── diagrama-datos.png
│   ├── 01-requerimientos.md
│   ├── 02-casos-de-uso.md
│   ├── 03-diagrama-clases.md
│   ├── 04-diagrama-datos.md
│   └── 05-gestion-proyecto.md
│
├── videojuegos.JSON   
├── .gitignore
└── README.md          # README principal
