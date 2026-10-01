import json
import time
from XVERSE_TP_03 import ArbolBinarioBusqueda, Videojuego


# Funciones
def buscar_secuencial(juegos, titulo):
    for j in juegos:
        if j["titulo"].lower() == titulo.lower():
            return j
    return None

def medir_tiempo(func, *args):
    inicio = time.time()
    resultado = func(*args)
    fin = time.time()
    return resultado, (fin - inicio) * 1000   

def preparar_arbol(juegos):
    arbol = ArbolBinarioBusqueda()
    for j in juegos:
        juego_obj = Videojuego(
            j["titulo"], j["genero"], j["rating"],
            j["año"], j["desarrollador"], j["descripcion"]
        )
        arbol.insertar(juego_obj)
    return arbol


# Cargar datasets
with open("juegos_100.json", "r", encoding="utf-8") as f:
    juegos_100 = json.load(f)
with open("juegos_1000.json", "r", encoding="utf-8") as f:
    juegos_1000 = json.load(f)
with open("juegos_10000.json", "r", encoding="utf-8") as f:
    juegos_10000 = json.load(f)

#  Experimentos
for juegos, n in [(juegos_100, 100), (juegos_1000, 1000), (juegos_10000, 10000)]:
    titulo_a_buscar = f"Juego {n//2}"

    # Secuencial
    _, t_seq = medir_tiempo(buscar_secuencial, juegos, titulo_a_buscar)

    # Árbol
    arbol = preparar_arbol(juegos)
    _, t_arbol = medir_tiempo(arbol.buscar, titulo_a_buscar)

    print(f"{n} elementos -> Secuencial: {t_seq:.4f} ms | Árbol: {t_arbol:.4f} ms")

