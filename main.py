from moduloClinica import registrarPaciente, asignarMedico, resumenPorMedico, listaPacientes

def menu():
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Registrar paciente")
        print("2. Asignar médico y diagnóstico")
        print("3. Ver resumen por médico")
        print("4. Ver pacientes registrados")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrarPaciente()
        elif opcion == "2":
            asignarMedico()
        elif opcion == "3":
            resumenPorMedico()
        elif opcion == "4":
            for paciente in listaPacientes:
                print(f"{paciente['nombre']} {paciente['apellido']} - Clasificación: {paciente['color']} - Emergencia: {'Sí' if paciente['emergencia'] else 'No'}")
        elif opcion == "5":
            print("Hasta luego.")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()