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
        print(f"{j['titulo']} ({j['genero']}, {j['plataforma']}) ★ {j['rating']}")

def buscar_juego(data, titulo):
    encontrados = [j for j in data if titulo.lower() in j['titulo'].lower()]
    if encontrados:
        listar_juegos(encontrados)
    else:
        print("No se encontró ningún juego con ese título.")

def filtrar_por_genero(data, genero):
    filtrados = [j for j in data if genero.lower() in j['genero'].lower()]
    listar_juegos(filtrados)


def filtrar_por_plataforma(data, plataforma):
    filtrados = [j for j in data if j['plataforma'].lower() == plataforma.lower()]
    listar_juegos(filtrados)




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



# Menú principal
while True:
    print("\n--- MENÚ XVerse ---")
    print("1. Listar todos los juegos")
    print("2. Buscar por título")
    print("3. Filtrar por género")
    print("4. Filtrar por plataforma")
    print("5. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        listar_juegos(juegos)
    elif opcion == "2":
        titulo = input("Título a buscar: ")
        buscar_juego(juegos, titulo)
    elif opcion == "3":
        genero = input("Género: ")
        filtrar_por_genero(juegos, genero)
    elif opcion == "4":
        plataforma = input("Plataforma: ")
        filtrar_por_plataforma(juegos, plataforma)
    elif opcion == "5":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida, intenta de nuevo.")



