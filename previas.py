import json

# Función para cargar datos de estudiantes desde un archivo JSON
def cargar_estudiantes(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            datos = json.load(archivo)
        return datos
    except FileNotFoundError:
        return []

# Función para buscar un estudiante en la lista de estudiantes
def buscar_estudiante(estudiantes, nombre):
    for estudiante in estudiantes:
        if estudiante['nombres'] == nombre:
            return estudiante
    return None

# Función para guardar las notas en un archivo JSON
def guardar_notas(notas):
    with open('notas.json', 'w') as archivo:
        json.dump(notas, archivo)

# Función para ingresar las notas y calcular promedio de un módulo
def ingresar_notas_modulo(nombre_modulo):
    print(f"Ingrese las notas para el módulo {nombre_modulo}:")
    nota1 = float(input("Ingrese la primera nota: "))
    nota2 = float(input("Ingrese la segunda nota: "))
    nota3 = float(input("Ingrese la tercera nota: "))

    # Calcular promedio
    promedio = (nota1 + nota2 + nota3) / 3

    # Solicitar ruta de estudio
    ruta_estudio = input("Ingrese la ruta de estudio: ")

    return {"nombre_modulo": nombre_modulo, "nota1": nota1, "nota2": nota2, "nota3": nota3, "promedio": promedio, "ruta_estudio": ruta_estudio}

# Función principal
def main():
    # Cargar datos de estudiantes
    estudiantes = cargar_estudiantes('estudiantes.json')

    # Solicitar nombre del estudiante a buscar
    nombre_estudiante = input("Ingrese el nombre del estudiante a buscar: ")

    # Buscar al estudiante
    estudiante = buscar_estudiante(estudiantes, nombre_estudiante)

    if estudiante:
        # Lista de módulos
        modulos = ["Módulo 1", "Módulo 2", "Módulo 3", "Módulo 4", "Módulo 5"]

        # Mostrar los módulos disponibles
        print("Módulos disponibles:")
        for i, modulo in enumerate(modulos, start=1):
            print(f"{i}. {modulo}")

        # Solicitar al usuario que elija un módulo
        opcion_modulo = int(input("Seleccione el módulo (1-5): "))
        if opcion_modulo not in range(1, 6):
            print("Opción inválida. Saliendo del programa.")
            return

        nombre_modulo_elegido = modulos[opcion_modulo - 1]

        # Ingresar las notas para el módulo elegido
        notas_modulo = ingresar_notas_modulo(nombre_modulo_elegido)

        # Guardar las notas en un archivo JSON
        guardar_notas(notas_modulo)

        print("Notas del módulo guardadas exitosamente.")
    else:
        print("Estudiante no encontrado.")

if __name__ == "__main__":
    main()
