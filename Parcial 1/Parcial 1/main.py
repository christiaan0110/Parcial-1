class Articulo:
    def __init__(self, id, nombre, precio):
        self.id = id
        self.nombre = nombre
        self.precio = precio

def mostrar_menu():
    print("\nOpciones del sistema de registro de presupuesto:")
    print("1. Registrar artículo")
    print("2. Buscar artículo")
    print("3. Editar artículo")
    print("4. Eliminar artículo")
    print("5. Salir")

def registrar_articulo(articulos):
    id = input("Ingrese el ID del artículo: ")
    nombre = input("Ingrese el nombre del artículo: ")
    precio = float(input("Ingrese el precio del artículo: "))
    articulos.append(Articulo(id, nombre, precio))
    print("Artículo registrado con éxito.")

def buscar_articulo(articulos):
    id = input("Ingrese el ID del artículo a buscar: ")
    for articulo in articulos:
        if articulo.id == id:
            print(f"ID: {articulo.id}, Nombre: {articulo.nombre}, Precio: {articulo.precio}")
            return
    print("Artículo no encontrado.")

def editar_articulo(articulos):
    id = input("Ingrese el ID del artículo a editar: ")
    for articulo in articulos:
        if articulo.id == id:
            articulo.nombre = input("Ingrese el nuevo nombre del artículo: ")
            articulo.precio = float(input("Ingrese el nuevo precio del artículo: "))
            print("Artículo editado con éxito.")
            return
    print("Artículo no encontrado.")

def eliminar_articulo(articulos):
    id = input("Ingrese el ID del artículo a eliminar: ")
    for articulo in articulos:
        if articulo.id == id:
            articulos.remove(articulo)
            print("Artículo eliminado con éxito.")
            return
    print("Artículo no encontrado.")

def main():
    articulos = []
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            registrar_articulo(articulos)
        elif opcion == '2':
            buscar_articulo(articulos)
        elif opcion == '3':
            editar_articulo(articulos)
        elif opcion == '4':
            eliminar_articulo(articulos)
        elif opcion == '5':
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("Opción inválida, por favor intente de nuevo.")

if __name__ == "__main__":
    main()