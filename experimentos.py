import json
import time


#Busqueda secuencial

def buscar_secuencial(juegos, titulo):
    for j in juegos:
        if j["titulo"].lower() == titulo.lower():
            return j
    return None


#Arbol binario de búsqueda

class Nodo:
    def __init__(self, juego):
        self.juego = juego
        self.izq = None
        self.der = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, juego):
        self.raiz = self._insertar(self.raiz, juego)

    def _insertar(self, nodo, juego):
        if nodo is None:
            return Nodo(juego)
        if juego["titulo"].lower() < nodo.juego["titulo"].lower():
            nodo.izq = self._insertar(nodo.izq, juego)
        else:
            nodo.der = self._insertar(nodo.der, juego)
        return nodo

    def buscar(self, titulo):
        return self._buscar(self.raiz, titulo.lower())

    def _buscar(self, nodo, titulo):
        if nodo is None:
            return None
        if nodo.juego["titulo"].lower() == titulo:
            return nodo.juego
        elif titulo < nodo.juego["titulo"].lower():
            return self._buscar(nodo.izq, titulo)
        else:
            return self._buscar(nodo.der, titulo)

#Busqueda binaria sobre lista ordenada
def busqueda_binaria(juegos, titulo):
    juegos_ordenados = sorted(juegos, key=lambda j: j["titulo"].lower())
    izquierda, derecha = 0, len(juegos_ordenados) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if juegos_ordenados[medio]["titulo"].lower() == titulo.lower():
            return juegos_ordenados[medio]
        elif juegos_ordenados[medio]["titulo"].lower() < titulo.lower():
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return None

#Busqueda binaria sobre lista ordenada con recursividad
def busqueda_binaria_recursiva(juegos, titulo, izquierda=0, derecha=None):
    if derecha is None:
        derecha = len(juegos) - 1
    if izquierda > derecha:
        return None
    medio = (izquierda + derecha) // 2
    if juegos[medio]["titulo"].lower() == titulo.lower():
        return juegos[medio]
    elif juegos[medio]["titulo"].lower() < titulo.lower():
        return busqueda_binaria_recursiva(juegos, titulo, medio + 1, derecha)
    else:
        return busqueda_binaria_recursiva(juegos, titulo, izquierda, medio - 1)

# Funcion para medir tiempo

def medir_tiempo(func, *args):
    inicio = time.time()
    resultado = func(*args)
    fin = time.time()
    return resultado, (fin - inicio) * 1000  # tiempo en ms


# Cargar datasets

with open("juegos_100.json", "r", encoding="utf-8") as f:
    juegos_100 = json.load(f)
with open("juegos_1000.json", "r", encoding="utf-8") as f:
    juegos_1000 = json.load(f)
with open("juegos_10000.json", "r", encoding="utf-8") as f:
    juegos_10000 = json.load(f)


# Experimentos

print("Resultados de los experimentos:\n")
for juegos, n in [(juegos_100, 100),
                  (juegos_1000, 1000),
                  (juegos_10000, 10000)]:

    # Árbol binario con todos los juegos
    arbol = ArbolBinario()
    for j in juegos:
        arbol.insertar(j)

    # Medir tiempos
    _, t_seq = medir_tiempo(buscar_secuencial, juegos, "Juego 50")
    _, t_bin = medir_tiempo(busqueda_binaria, juegos, "Juego 50")
    _, t_bin_rec = medir_tiempo(busqueda_binaria_recursiva, juegos, "Juego 50")
    _, t_arbol = medir_tiempo(arbol.buscar, "Juego 50")

    print(f"{n} elementos -> Secuencial: {t_seq:.4f} ms | Binaria: {t_bin:.4f} ms | Binaria Recursiva: {t_bin_rec:.4f} ms | Árbol: {t_arbol:.4f} ms")
