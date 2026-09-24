import json

# Abrir y cargar el dataset
with open("videojuegos.json", "r", encoding="utf-8") as f:
    juegos = json.load(f)

# Mostrar todos los juegos
for juego in juegos:
    print(f"{juego['titulo']} ({juego['genero']}, {juego['plataforma']}) ⭐{juego['rating']}")
