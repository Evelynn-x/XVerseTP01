import json

# Abrir y cargar el dataset
with open("videojuegos.json", "r", encoding="utf-8") as f:
    juegos = json.load(f)


import json

# Cargar dataset
with open("videojuegos.json", "r", encoding="utf-8") as f:
    juegos = json.load(f)

def listar_juegos(data):
    for j in data:
        print(f"{j['titulo']} ({j['genero']}) ★ {j['rating']}")
        print(f"   Año: {j['año']}")
        print(f"   Desarrollador: {j['desarrollador']}")
        print(f"   Descripción: {j['descripcion']}\n")

def buscar_juego(data, titulo):
    encontrados = [j for j in data if titulo.lower() in j['titulo'].lower()]
    if encontrados:
        listar_juegos(encontrados)
    else:
        print("No se encontró ningún juego con ese título.")

def filtrar_por_genero(data, genero):
    filtrados = [j for j in data if genero.lower() in j['genero'].lower()]
    if filtrados:
        listar_juegos(filtrados)
    else:
        print("No se encontraron juegos de ese género.")




class Videojuego:
    def __init__(self, titulo, genero, rating, año, desarrollador, descripcion):
        self._titulo = titulo
        self._genero = genero
        self._rating = rating
        self._año = año
        self._desarrollador = desarrollador
        self._descripcion = descripcion

    def __repr__(self):
        return (f"{self._titulo} ({self._genero}) ⭐{self._rating}\n"
                f"   Año: {self._año}\n"
                f"   Desarrollador: {self._desarrollador}\n"
                f"   Descripción: {self._descripcion}\n")


#convierte el dataset en una lista de objetos Videojuego
import json

with open("videojuegos.json", "r", encoding="utf-8") as f:
    data = json.load(f)

juegos = [
    Videojuego(
        j["titulo"],
        j["genero"],
        j["rating"],
        j["año"],
        j["desarrollador"],
        j["descripcion"]
    )
    for j in data
]





#funciones para listar, buscar y filtrar juegos

def listar_juegos(data):
    for j in data:
        print(j)

def buscar_juego(data, titulo):
    encontrados = [j for j in data if titulo.lower() in j._titulo.lower()]
    if encontrados:
        listar_juegos(encontrados)
    else:
        print("No se encontró ningún juego con ese título.")

def filtrar_por_genero(data, genero):
    filtrados = [j for j in data if genero.lower() in j._genero.lower()]
    listar_juegos(filtrados)

def ver_top_10(juegos):
    # Ordena los juegos por rating de mayor a menor
    juegos_ordenados = sorted(juegos, key=lambda x: x._rating, reverse=True)
    print("\n--- TOP 10 JUEGOS ---")
    for i, juego in enumerate(juegos_ordenados[:10], start=1):
        print(f"{i}. {juego._titulo} ({juego._genero}) ⭐{juego._rating}")
        print(f"   Año: {juego._año}")
        print(f"   Desarrollador: {juego._desarrollador}")
        print(f"   Descripción: {juego._descripcion}\n")

def juegos_relacionados(juegos, titulo):
    # Busca el juego por título
    juego_base = next((j for j in juegos if j._titulo.lower() == titulo.lower()), None)
    if not juego_base:
        print("Juego no encontrado.")
        return

    relacionados = [
        j for j in juegos
        if j._genero.lower() == juego_base._genero.lower() and j._titulo.lower() != titulo.lower()
    ]
    if relacionados:
        listar_juegos(relacionados)
    else:
        print("No se encontraron juegos relacionados.")

def buscar_por_año(data, año):
    encontrados = [j for j in data if j._año == año]
    if encontrados:
        for juego in encontrados:
            print(juego)
    else:
        print("No se encontraron juegos de ese año.")

def buscar_por_desarrollador(data, desarrollador):
    encontrados = [j for j in data if desarrollador.lower() in j._desarrollador.lower()]
    if encontrados:
        for juego in encontrados:
            print(juego)
    else:
        print("No se encontraron juegos de ese desarrollador.")

# Menú principal
while True:
    print("--- MENÚ XVerse ---")
    print("1. Listar todos los juegos")
    print("2. Buscar por título")
    print("3. Ver Top 10")
    print("4. Ver juegos relacionados")
    print("5. Filtrar por género")
    print("6. Buscar por año")
    print("7. Buscar por desarrollador")
    print("8. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        listar_juegos(juegos)
    elif opcion == "2":
        titulo = input("Título a buscar: ")
        buscar_juego(juegos, titulo)
    elif opcion == "3":
        ver_top_10(juegos)
    elif opcion == "4":
        titulo = input("Título para ver relacionados: ")
        juegos_relacionados(juegos, titulo)
    elif opcion == "5":
        genero = input("Género: ")
        filtrar_por_genero(juegos, genero)
    elif opcion == "6":
        año = int(input("Año a buscar: "))
        buscar_por_año(juegos, año)
    elif opcion == "7":
        desarrollador = input("Desarrollador a buscar: ")
        buscar_por_desarrollador(juegos, desarrollador)
    elif opcion == "8":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida, intenta de nuevo.")