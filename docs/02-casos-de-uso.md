# 📄 Proyecto XVerse - Casos de Uso

##  Introducción
Este documento describe los principales casos de uso del sistema XVerse.  
Cada caso de uso representa una interacción típica entre el usuario y el sistema, mostrando cómo se cumplen los requerimientos funcionales.

---

##  Caso de uso 1: Listar todos los juegos
**Actor principal:** Usuario  
**Objetivo:** Visualizar el catálogo completo de videojuegos.  
**Flujo principal:**
1. El usuario ejecuta el programa.
2. Selecciona la opción "Listar juegos".
3. El sistema recorre el dataset y muestra todos los títulos con sus datos (género, año, desarrollador, rating).  

---

##  Caso de uso 2: Buscar juego por título (búsqueda secuencial)
**Actor principal:** Usuario  
**Objetivo:** Encontrar un videojuego específico por su nombre.  
**Flujo principal:**
1. El usuario selecciona la opción "Buscar por título (secuencial)".
2. Ingresa el nombre del juego.
3. El sistema recorre la lista secuencialmente hasta encontrar coincidencia.
4. Muestra los datos del juego encontrado.  

---

##  Caso de uso 3: Buscar juego por título (árbol binario)
**Actor principal:** Usuario  
**Objetivo:** Encontrar un videojuego específico usando el árbol binario.  
**Flujo principal:**
1. El usuario selecciona la opción "Buscar por título (árbol)".
2. Ingresa el nombre del juego.
3. El sistema recorre el árbol binario de búsqueda.
4. Muestra los datos del juego encontrado.  

---

##  Caso de uso 4: Filtrar juegos por género
**Actor principal:** Usuario  
**Objetivo:** Ver únicamente los juegos de un género específico.  
**Flujo principal:**
1. El usuario selecciona la opción "Filtrar por género".
2. Ingresa el género deseado (ejemplo: RPG).
3. El sistema recorre el dataset y muestra solo los juegos que pertenecen a ese género.  

---

##  Caso de uso 5: Ejecutar experimentos de rendimiento (TP2)
**Actor principal:** Usuario  
**Objetivo:** Comparar tiempos de ejecución entre distintos métodos de búsqueda.  
**Flujo principal:**
1. El usuario ejecuta el script `experimentos.py`.
2. El sistema carga los datasets de 100, 1000 y 10000 juegos.
3. Ejecuta búsquedas con distintos métodos (secuencial, binaria, árbol, diccionario).
4. Mide tiempos y muestra resultados comparativos en consola.  

---

##  Conclusión
Estos casos de uso reflejan las principales interacciones del usuario con el sistema XVerse hasta el **TP03**, incluyendo las pruebas de rendimiento del **TP02**.  
En las futuras etapas (TP04 a TP10) se agregarán nuevos casos de uso relacionados con estructuras avanzadas y funcionalidades extendidas.
