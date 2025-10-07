import csv
import os

# Archivo CSV para persistencia
ARCHIVO_CSV = "catalogo.csv"


def cargar_datos():
    """Carga los datos del archivo CSV y devuelve las listas paralelas"""
    titulos, ejemplares = [], []
    if os.path.exists(ARCHIVO_CSV):
        with open(ARCHIVO_CSV, 'r', encoding='utf-8') as archivo:
            lector = csv.reader(archivo)
            for fila in lector:
                if len(fila) == 2:
                    titulos.append(fila[0])
                    ejemplares.append(int(fila[1]))
    return titulos, ejemplares


def guardar_datos(titulos, ejemplares):
    """Guarda los datos de las listas paralelas en el archivo CSV"""
    with open(ARCHIVO_CSV, 'w', encoding='utf-8', newline='') as archivo:
        escritor = csv.writer(archivo)
        for i in range(len(titulos)):
            escritor.writerow([titulos[i], ejemplares[i]])


def ingresar_titulos(titulos, ejemplares):
    """Opción 1: Ingresar títulos iniciales"""
    print("\n--- Ingresar Títulos ---")
    cantidad = input("¿Cuántos títulos desea ingresar? ")

    if not cantidad.isdigit():
        print("Error: Debe ingresar un número válido")
        return titulos, ejemplares

    cantidad = int(cantidad)

    for i in range(cantidad):
        titulo = input(f"Ingrese el título #{i+1}: ").strip()
        if titulo:
            titulos.append(titulo)
            ejemplares.append(0)
        else:
            print("Error: El título no puede estar vacío")

    guardar_datos(titulos, ejemplares)
    print(f"\n{cantidad} título(s) agregado(s) exitosamente")
    return titulos, ejemplares


def ingresar_ejemplares(titulos, ejemplares):
    """Opción 2: Ingresar ejemplares para cada título"""
    if not titulos:
        print("\nNo hay títulos registrados. Primero ingrese títulos.")
        return titulos, ejemplares

    print("\n--- Ingresar Ejemplares ---")
    print("Títulos disponibles:")
    for i in range(len(titulos)):
        print(f"{i+1}. {titulos[i]} (Ejemplares actuales: {ejemplares[i]})")

    indice = input("\nSeleccione el número del título: ")

    if not indice.isdigit():
        print("Error: Debe ingresar un número válido")
        return titulos, ejemplares

    indice = int(indice) - 1

    if indice < 0 or indice >= len(titulos):
        print("Error: Número de título inválido")
        return titulos, ejemplares

    cantidad = input(f"¿Cuántos ejemplares desea agregar a '{titulos[indice]}'? ")

    if not cantidad.isdigit():
        print("Error: Debe ingresar un número válido")
        return titulos, ejemplares

    cantidad = int(cantidad)
    ejemplares[indice] += cantidad

    guardar_datos(titulos, ejemplares)
    print(f"\nEjemplares actualizados. Total ahora: {ejemplares[indice]}")
    return titulos, ejemplares


def mostrar_catalogo(titulos, ejemplares):
    """Opción 3: Mostrar catálogo completo"""
    if not titulos:
        print("\nEl catálogo está vacío")
        return

    print("\n--- Catálogo de la Biblioteca ---")
    print(f"{'#':<5} {'Título':<40} {'Ejemplares':<12}")
    print("-" * 57)

    for i in range(len(titulos)):
        print(f"{i+1:<5} {titulos[i]:<40} {ejemplares[i]:<12}")


def consultar_disponibilidad(titulos, ejemplares):
    """Opción 4: Consultar disponibilidad de un título específico"""
    if not titulos:
        print("\nEl catálogo está vacío")
        return

    print("\n--- Consultar Disponibilidad ---")
    busqueda = input("Ingrese el título a buscar: ").strip().lower()

    encontrado = False
    for i in range(len(titulos)):
        if busqueda in titulos[i].lower():
            print(f"\nTítulo: {titulos[i]}")
            print(f"Ejemplares disponibles: {ejemplares[i]}")
            encontrado = True

    if not encontrado:
        print("\nNo se encontró ningún título con ese nombre")


def listar_agotados(titulos, ejemplares):
    """Opción 5: Listar títulos agotados (0 ejemplares)"""
    if not titulos:
        print("\nEl catálogo está vacío")
        return

    print("\n--- Títulos Agotados ---")
    agotados = [titulos[i] for i in range(len(titulos)) if ejemplares[i] == 0]

    if not agotados:
        print("No hay títulos agotados")
    else:
        for titulo in agotados:
            print(f"- {titulo}")


def agregar_titulo(titulos, ejemplares):
    """Opción 6: Agregar un nuevo título al catálogo"""
    print("\n--- Agregar Nuevo Título ---")
    titulo = input("Ingrese el título del libro: ").strip()

    if not titulo:
        print("Error: El título no puede estar vacío")
        return titulos, ejemplares

    cantidad = input("¿Cuántos ejemplares tiene este título? ")

    if not cantidad.isdigit():
        print("Error: Debe ingresar un número válido")
        return titulos, ejemplares

    cantidad = int(cantidad)

    titulos.append(titulo)
    ejemplares.append(cantidad)

    guardar_datos(titulos, ejemplares)
    print(f"\nTítulo '{titulo}' agregado con {cantidad} ejemplar(es)")
    return titulos, ejemplares


def actualizar_ejemplares(titulos, ejemplares):
    """Opción 7: Actualizar ejemplares (préstamo/devolución)"""
    if not titulos:
        print("\nEl catálogo está vacío")
        return titulos, ejemplares

    print("\n--- Actualizar Ejemplares ---")
    for i in range(len(titulos)):
        print(f"{i+1}. {titulos[i]} ({ejemplares[i]} ejemplares)")

    indice = input("\nSeleccione el número del título: ")

    if not indice.isdigit():
        print("Error: Debe ingresar un número válido")
        return titulos, ejemplares

    indice = int(indice) - 1

    if indice < 0 or indice >= len(titulos):
        print("Error: Número de título inválido")
        return titulos, ejemplares

    print(f"\nTítulo seleccionado: {titulos[indice]}")
    print(f"Ejemplares actuales: {ejemplares[indice]}")
    print("\n1. Préstamo (disminuir)")
    print("2. Devolución (aumentar)")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        if ejemplares[indice] > 0:
            ejemplares[indice] -= 1
            guardar_datos(titulos, ejemplares)
            print(f"\nPréstamo registrado. Ejemplares restantes: {ejemplares[indice]}")
        else:
            print("\nError: No hay ejemplares disponibles para préstamo")
    elif opcion == "2":
        ejemplares[indice] += 1
        guardar_datos(titulos, ejemplares)
        print(f"\nDevolución registrada. Ejemplares actuales: {ejemplares[indice]}")
    else:
        print("\nOpción inválida")

    return titulos, ejemplares


def mostrar_menu():
    """Muestra el menú principal"""
    print("\n" + "="*50)
    print("SISTEMA DE GESTIÓN DE BIBLIOTECA ESCOLAR")
    print("="*50)
    print("1. Ingresar títulos")
    print("2. Ingresar ejemplares")
    print("3. Mostrar catálogo")
    print("4. Consultar disponibilidad")
    print("5. Listar agotados")
    print("6. Agregar título")
    print("7. Actualizar ejemplares (préstamo/devolución)")
    print("8. Salir")
    print("="*50)


def main():
    """Función principal del programa"""
    titulos, ejemplares = cargar_datos()
    continuar = True

    while continuar:
        mostrar_menu()
        opcion = input("\nSeleccione una opción: ")

        match opcion:
            case "1":
                titulos, ejemplares = ingresar_titulos(titulos, ejemplares)
            case "2":
                titulos, ejemplares = ingresar_ejemplares(titulos, ejemplares)
            case "3":
                mostrar_catalogo(titulos, ejemplares)
            case "4":
                consultar_disponibilidad(titulos, ejemplares)
            case "5":
                listar_agotados(titulos, ejemplares)
            case "6":
                titulos, ejemplares = agregar_titulo(titulos, ejemplares)
            case "7":
                titulos, ejemplares = actualizar_ejemplares(titulos, ejemplares)
            case "8":
                print("\nGracias por usar el sistema. ¡Hasta luego!")
                continuar = False
            case _:
                print("\nOpción inválida. Por favor, seleccione una opción del 1 al 8")


if __name__ == "__main__":
    main()
