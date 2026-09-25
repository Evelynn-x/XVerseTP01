import json

# Abrir y cargar el dataset
with open("videojuegos.json", "r", encoding="utf-8") as f:
    juegos = json.load(f)

# Mostrar todos los juegos
for juego in juegos:
    print(f"{juego['titulo']} ({juego['genero']}, {juego['plataforma']}) ⭐{juego['rating']}")



import json

# Cargar dataset
with open("videojuegos.json", "r", encoding="utf-8") as f:
    juegos = json.load(f)

def listar_juegos(data):
    for j in data:
        print(f"{j['titulo']} ({j['genero']}) ★ {j['rating']}")
        print(f"   Año: {j['año']}")
        print(f"   Desarrollador: {j['desarrollador']}")
        print(f"   Exclusivo: {'Sí' if j['exclusivo'] else 'No'}")
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
    def __init__(self, titulo, genero, plataforma, rating):
        self._titulo = titulo
        self._genero = genero
        self._plataforma = plataforma
        self._rating = rating

    def __repr__(self):
        return f"{self._titulo} ({self._genero}, {self._plataforma}) ⭐{self._rating}"



import json

with open("videojuegos.json", "r", encoding="utf-8") as f:
    data = json.load(f)

juegos = [Videojuego(j["titulo"], j["genero"], j["plataforma"], j["rating"]) for j in data]

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

def filtrar_por_plataforma(data, plataforma):
    filtrados = [j for j in data if plataforma.lower() in j._plataforma.lower()]
    listar_juegos(filtrados)

def ver_top_10(juegos):
    # Ordena los juegos por rating de mayor a menor
    juegos_ordenados = sorted(juegos, key=lambda x: x["rating"], reverse=True)
    print("\n--- TOP 10 JUEGOS ---")
    for i, juego in enumerate(juegos_ordenados[:10], start=1):
        print(f"{i}. {juego['titulo']} ({juego['consola']}) ⭐{juego['rating']}")

def juegos_relacionados(juegos, titulo):
    # Busca el juego por título
    juego_base = next((j for j in juegos if j["titulo"].lower() == titulo.lower()), None)
    if not juego_base:
        print("Juego no encontrado.")
        return

    

# Menú principal
while True:
    print("\n--- MENÚ XVerse ---")
    print("1. Listar todos los juegos")
    print("2. Buscar por título")
    print("3. Ver Top 10")
    print("4. Ver juegos relacionados")
    print("5. Filtrar por género")
    print("6. Salir")

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
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida, intenta de nuevo.")



