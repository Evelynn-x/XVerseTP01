import json

def generar_juegos(cantidad):
    juegos = []
    for i in range(cantidad):
        juego = {
            "titulo": f"Juego {i+1}",
            "genero": "Acción",
            "rating": (i % 10) + 1,  # rating entre 1 y 10
            "año": 2000 + (i % 25),  # años entre 2000 y 2025
            "desarrollador": f"Dev {i % 50}",
            "descripcion": "Juego generado automáticamente"
        }
        juegos.append(juego)
    return juegos

# Generar 10.000 juegos
juegos_10000 = generar_juegos(10000)

# Guardar en archivo JSON
with open("juegos_10000.json", "w", encoding="utf-8") as f:
    json.dump(juegos_10000, f, ensure_ascii=False, indent=4)

print("Archivo juegos_10000.json creado con 10.000 juegos de prueba.")