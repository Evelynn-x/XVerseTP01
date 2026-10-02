import json
import os

# Cargar dataset desde la raíz del proyecto
base_dir = os.path.dirname(__file__)   # carpeta TP03
ruta_json = os.path.join(base_dir, "..", "videojuegos.json")

with open(ruta_json, "r", encoding="utf-8") as f:
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



#clases para el árbol binario de búsqueda 
class Nodo:
    def __init__(self, juego):
        self.juego = juego
        self.izq = None
        self.der = None

class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    def insertar(self, juego):
        def _insertar(nodo, juego):
            if nodo is None:
                return Nodo(juego)
            if juego._titulo.lower() < nodo.juego._titulo.lower():
                nodo.izq = _insertar(nodo.izq, juego)
            else:
                nodo.der = _insertar(nodo.der, juego)
            return nodo
        self.raiz = _insertar(self.raiz, juego)

    def buscar(self, titulo):
        def _buscar(nodo, titulo):
            if nodo is None:
                return None
            if titulo.lower() == nodo.juego._titulo.lower():
                return nodo.juego
            elif titulo.lower() < nodo.juego._titulo.lower():
                return _buscar(nodo.izq, titulo)
            else:
                return _buscar(nodo.der, titulo)
        return _buscar(self.raiz, titulo)

    # Recorrido inorder (izq - raíz - der)
    def inorder(self):
        def _inorder(nodo):
            if nodo:
                _inorder(nodo.izq)
                print(nodo.juego)
                _inorder(nodo.der)
        _inorder(self.raiz)

    # Recorrido preorder (raíz - izq - der)
    def preorder(self):
        def _preorder(nodo):
            if nodo:
                print(nodo.juego)
                _preorder(nodo.izq)
                _preorder(nodo.der)
        _preorder(self.raiz)

    # Recorrido postorder (izq - der - raíz)
    def postorder(self):
        def _postorder(nodo):
            if nodo:
                _postorder(nodo.izq)
                _postorder(nodo.der)
                print(nodo.juego)
        _postorder(self.raiz)




#convierte el dataset en una lista de objetos Videojuego

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



# Construcción del árbol binario con los juegos
arbol = ArbolBinarioBusqueda()
for juego in juegos:
    arbol.insertar(juego)



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
def ejecutar_menu():
    while True:
        print("--- MENÚ XVerse TP3 ---")
        print("1. Listar todos los juegos (secuencial)")
        print("2. Buscar por título (secuencial)")
        print("3. Ver Top 10")
        print("4. Ver juegos relacionados (preorder)")
        print("5. Filtrar por género (inorder)")
        print("6. Buscar por año (postorder)")
        print("7. Buscar por desarrollador (postorder)")
        print("8. Buscar por título con árbol")
        print("9. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            listar_juegos(juegos)
        elif opcion == "2":
            titulo = input("Título a buscar: ")
            buscar_juego(juegos, titulo)
        elif opcion == "3":
            ver_top_10(juegos)
        elif opcion == "4":
            arbol.preorder()
        elif opcion == "5":
            arbol.inorder()
        elif opcion == "6":
            arbol.postorder()
        elif opcion == "7":
            arbol.postorder()
        elif opcion == "8":
            titulo = input("Título a buscar: ")
            resultado = arbol.buscar(titulo)
            print(resultado if resultado else "No encontrado en árbol.")
        elif opcion == "9":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida, intenta de nuevo.")

#No se ejecuta el menú si el archivo es importado como módulo
if __name__ == "__main__":
    ejecutar_menu()
