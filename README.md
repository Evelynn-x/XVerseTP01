# ✳ Proyecto XVerse

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

## 🚀 Uso del programa
Para ejecutar cada versión desde la terminal:

### TP01 (versión inicial)
```bash
py XVERSE-TP-01.py

---

## Estructura del repositorio

PROYECTO XVERSE/
├── XVERSE-TP-01.py          # Menú básico con búsqueda secuencial
├── XVERSE-TP-03.py          # Versión extendida con árbol binario
├── videojuegos.json         # Dataset principal
├── experimentos.py          # Script de pruebas de rendimiento
├── generar_dataset.py       # Generador de datasets
├── juegos_100.json          # Dataset pequeño
├── juegos_1000.json         # Dataset mediano
├── juegos_10000.json        # Dataset grande
├── README.md                # README principal 

├── TP2/
│   ├── README.md             # Explicación del TP2

├── docs/
│   ├── 01-requerimientos.md  # Documentación del proyecto
│   ├── 02-casos-de-uso.md
│   ├── 03-diagrama-clases.md # Explicación + imagen UML
│   ├── 04-diagrama-datos.md  # Conexión datasets y estructuras
│   ├── 05-gestion-proyecto.md
│   ├── capturas/             # Carpeta de imágenes exportadas
│   │   ├── diagrama-clases.png
│   │   ├── diagrama-datos.png
