# 📄 Proyecto XVerse - Requerimientos

## 📌 Requerimientos funcionales
El sistema debe permitir:
1. Cargar datasets de videojuegos desde archivos JSON.
2. Listar todos los juegos con sus datos (título, género, año, desarrollador, rating, descripción).
3. Buscar juegos por título (búsqueda secuencial y búsqueda con árbol binario).
4. Filtrar juegos por género.
5. Buscar juegos por año de lanzamiento.
6. Buscar juegos por desarrollador.
7. Mostrar un Top 10 de juegos según rating.
8. Mostrar juegos relacionados (misma saga o desarrollador).
9. Ejecutar recorridos del árbol binario (inorder, preorder, postorder).
10. Comparar resultados de búsqueda secuencial vs. árbol binario.
11. Ejecutar experimentos de rendimiento con datasets de 100, 1000 y 10000 juegos.

---

## 📌 Requerimientos no funcionales
- El sistema debe estar implementado en **Python 3.x**.
- El código debe ser modular y organizado en archivos separados (TP01, TP02, TP03).
- Los resultados deben mostrarse en consola con formato claro y legible.
- El sistema debe manejar correctamente la lectura de archivos JSON con codificación UTF-8.
- El tiempo de ejecución debe ser medido en los experimentos (TP2).

---

## 📌 Alcance
- Actualmente el proyecto abarca hasta el **TP03**, incluyendo:
  - Lectura de datasets.
  - Funciones de búsqueda y filtrado.
  - Árbol binario de búsqueda.
  - Experimentos de rendimiento con distintos tamaños de dataset.

- En futuras etapas se sumarán los **TP04 a TP10**, que ampliarán el sistema con nuevas estructuras de datos, algoritmos y funcionalidades avanzadas.

- El proyecto se limita a ejecución en consola y manejo de archivos locales (sin interfaz gráfica ni conexión a bases de datos externas).

---

## 📎 Conclusión
Este documento define los requisitos básicos del sistema XVerse.  
Los requerimientos funcionales aseguran que el usuario pueda interactuar con el catálogo de videojuegos, mientras que los no funcionales garantizan eficiencia, claridad y extensibilidad del código.
