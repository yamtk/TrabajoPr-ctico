datos = {
    "Alumnos": []
}

# Función para mostrar los datos de cada alumno
def mostrar_alumnos(datos):
    if not datos["Alumnos"]:
        print("No hay alumnos registrados.")
    else:
        for i, alumno in enumerate(datos["Alumnos"], start=1):
            print(f"Alumno {i}:")
            for clave, valor in alumno.items():
                print(f"  {clave}: {valor}")
            print("-" * 30)

# Función para agregar un alumno
def agregar_alumno(datos):
    alumno = {
        "Nombre": input("Nombre: "),
        "Apellido": input("Apellido: "),
        "DNI": input("DNI: "),
        "Fecha de nacimiento": input("Fecha de nacimiento (DD/MM/AAAA): "),
        "Tutor": input("Nombre del Tutor: "),
        "Notas": [],
        "Faltas": 0,
        "Amonestaciones": 0
    }
    datos["Alumnos"].append(alumno)
    print("Alumno agregado con éxito.")

# Función para modificar los datos de un alumno
def modificar_alumno(datos):
    mostrar_alumnos(datos)
    indice = int(input("Seleccione el número del alumno a modificar: ")) - 1
    if 0 <= indice < len(datos["Alumnos"]):
        alumno = datos["Alumnos"][indice]
        print("Deje en blanco para no modificar un campo.")
        for clave in alumno.keys():
            if clave in ["Notas", "Faltas", "Amonestaciones"]:
                continue
            nuevo_valor = input(f"{clave} (actual: {alumno[clave]}): ")
            if nuevo_valor:
                alumno[clave] = nuevo_valor
        print("Alumno modificado con éxito.")
    else:
        print("Índice no válido.")

# Función para expulsar un alumno
def expulsar_alumno(datos):
    mostrar_alumnos(datos)
    indice = int(input("Seleccione el número del alumno a expulsar: ")) - 1
    if 0 <= indice < len(datos["Alumnos"]):
        datos["Alumnos"].pop(indice)
        print("Alumno expulsado con éxito.")
    else:
        print("Índice no válido.")

# Función para registrar una nota, falta o amonestación a un alumno
def registrar_actividad(datos):
    mostrar_alumnos(datos)
    indice = int(input("Seleccione el número del alumno: ")) - 1
    if 0 <= indice < len(datos["Alumnos"]):
        print("1. Registrar nota")
        print("2. Registrar falta")
        print("3. Registrar amonestación")
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            nota = float(input("Ingrese la nota: "))
            datos["Alumnos"][indice]["Notas"].append(nota)
            print("Nota registrada con éxito.")
        elif opcion == 2:
            datos["Alumnos"][indice]["Faltas"] += 1
            print("Falta registrada con éxito.")
        elif opcion == 3:
            datos["Alumnos"][indice]["Amonestaciones"] += 1
            print("Amonestación registrada con éxito.")
        else:
            print("Opción no válida.")
    else:
        print("Índice no válido.")

# Menú principal
def menu():
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Mostrar alumnos")
        print("2. Agregar alumno")
        print("3. Modificar alumno")
        print("4. Expulsar alumno")
        print("5. Registrar actividad (nota, falta, amonestación)")
        print("6. Salir")
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            mostrar_alumnos(datos)
        elif opcion == 2:
            agregar_alumno(datos)
        elif opcion == 3:
            modificar_alumno(datos)
        elif opcion == 4:
            expulsar_alumno(datos)
        elif opcion == 5:
            registrar_actividad(datos)
        elif opcion == 6:
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida.")


menu()


#Lo hice con IA, hay varias partes que si logre entender, pero 
#hay otras en que no, me gustaría que repasemos el códico para terminar
#de entenderlo. Muchas gracias, y perdon por usar IA