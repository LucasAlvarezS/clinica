import random

listaPacientes = []
medicosDisponibles = ["Donald Trump", "Benjamín Netanyahu", "Alí Jamenei"]

def clasificarPaciente(sintomas):
    cantidad = len(sintomas)
    if cantidad <= 3:
        return "Verde"
    elif 4 <= cantidad <= 5:
        return "Amarillo"
    else:
        return "Rojo"

def registrarPaciente():
    try:
        nombre = input("Nombre: ").strip()
        apellido = input("Apellido: ").strip()
        edad = int(input("Edad: "))
        sexo = input("Sexo (M/F): ").strip().upper()
        temperatura = float(input("Temperatura corporal (°C): "))
        presionSis = int(input("Presión sistólica: "))
        presionDia = int(input("Presión diastólica: "))
        pulsaciones = int(input("Pulsaciones por minuto: "))
        
        if not nombre or not apellido or edad <= 0 or temperatura < 30 or temperatura > 45 or presionSis <= 0 or presionDia <= 0 or pulsaciones <= 0:
            raise ValueError("Alguno de los valores ingresados no es válido.")

        sintomasPosibles = [
            "fiebre", "presión alta", "presión baja", "dolor de cabeza", "malestar estomacal",
            "dolor muscular", "tos", "dolor de garganta", "náuseas", "vómitos",
            "congestión nasal", "fatiga", "mareos"
        ]

        sintomas = []
        if temperatura > 37.8:
            sintomas.append("fiebre")
        if presionSis > 140 or presionDia > 90:
            sintomas.append("presión alta")
        if presionSis < 90 or presionDia < 60:
            sintomas.append("presión baja")

        print("\nSíntomas posibles:")
        for s in sintomasPosibles:
            print(f"- {s}")
        print("- otros")

        while True:
            sintoma = input("Ingrese un síntoma (ENTER para terminar): ").strip().lower()
            if not sintoma:
                break
            if sintoma not in sintomas:
                sintomas.append(sintoma)

        color = clasificarPaciente(sintomas)
        emergencia = random.randint(1, 10) == 1
        if emergencia:
            print("ALERTA ROJA: Este paciente debe ingresar a quirófano de inmediato.")
        
        paciente = {
            "nombre": nombre,
            "apellido": apellido,
            "edad": edad,
            "sexo": sexo,
            "temperatura": temperatura,
            "presion": (presionSis, presionDia),
            "pulsaciones": pulsaciones,
            "sintomas": sintomas,
            "color": color,
            "emergencia": emergencia,
            "medico": None,
            "diagnostico": None,
            "tratamiento": None
        }

        listaPacientes.append(paciente)
        print("Paciente registrado correctamente.\n")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")

def asignarMedico():
    nombrePaciente = input("Nombre del paciente a asignar: ").strip()
    medico = input("Nombre del médico: ").strip()
    diagnostico = input("Diagnóstico: ").strip()
    tratamiento = input("Tratamiento propuesto: ").strip()

    for paciente in listaPacientes:
        if paciente["nombre"].lower() == nombrePaciente.lower():
            paciente["medico"] = medico
            paciente["diagnostico"] = diagnostico
            paciente["tratamiento"] = tratamiento
            print("Médico, diagnóstico y tratamiento asignados.")
            return

    print("Paciente no encontrado.")

def resumenPorMedico():
    resumen = {}
    for medico in medicosDisponibles:
        resumen[medico] = {"total": 0, "verde": 0, "amarillo": 0, "rojo": 0, "pacientes": []}

    for paciente in listaPacientes:
        medico = paciente.get("medico")
        if medico in resumen:
            resumen[medico]["total"] += 1
            resumen[medico][paciente["color"].lower()] += 1
            resumen[medico]["pacientes"].append(paciente)

    for medico, datos in resumen.items():
        print(f"\n Médico: {medico}")
        print(f"Total pacientes: {datos['total']} | Verde: {datos['verde']} | Amarillo: {datos['amarillo']} | Rojo: {datos['rojo']}")
        for p in datos["pacientes"]:
            print(f"- {p['nombre']} {p['apellido']} ({p['color']}): {p['diagnostico']} -> {p['tratamiento']}")
