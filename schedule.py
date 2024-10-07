import random

def asignacion_horarios():

    cursos = {
        'Taller_de_Programacion': 'Ing. Arturo Terceros',
        'Bases_de_Datos II': 'Ing. Osamu Yokosaki',
        'Inteligencia_Artificial': 'Lic. Marianela Loza',
        'Investigación_operativa':'Lic. Maritza Villa',
        'Redes_de_Computadoras':'Ing. Pablo Pacheco',
        'Analisis_y_Diseño_de_Sistemas':'Ing. Angela Santos'
    }
    
    salones = ['Salon_314']
    
    horarios = [
        'Lunes_7:45-10:00', 'Lunes_10:00-11:45',
        'Martes_7:45-10:00', 'Martes_10:00-11:45', 'Martes_12:00-2:15',
        'Miércoles_7:45-10:00', 'Miércoles_10:00-11:45',
        'Jueves_7:45-10:00', 'Jueves_10:00-11:45',
        'Viernes_7:45-10:00', 'Viernes_10:00-11:45', 'Viernes_12:00-2:15'
    ]

    random.shuffle(horarios)

    asignaciones = {}
    profesor_horario = {}
    salon_horario = {}

    for curso, profesor in cursos.items():
        asignado = 0  
        for horario_idx, horario in enumerate(horarios):
            
            # Comprobar si el profesor ya está ocupado en ese horario
            if profesor in profesor_horario and horario in profesor_horario[profesor]:
                continue 
            
            # Comprobar si el salón ya está ocupado en ese horario
            for salon in salones:
                if salon in salon_horario and horario in salon_horario[salon]:
                    continue 

                # Asignar el curso al horario y salón si no hay conflictos
                if curso not in asignaciones:
                    asignaciones[curso] = []
                
                asignaciones[curso].append((horario, salon))
                
                # Actualizar los horarios ocupados por el profesor y el salón
                if profesor in profesor_horario:
                    profesor_horario[profesor].append(horario)
                else:
                    profesor_horario[profesor] = [horario]

                if salon in salon_horario:
                    salon_horario[salon].append(horario)
                else:
                    salon_horario[salon] = [horario]

                asignado += 1
                if asignado == 2:
                    break 
                
            if asignado == 2:
                break 
    
    # Imprimir
    for curso, asignacion in asignaciones.items():
        print(f"Materia: {curso}")
        for horario, salon in asignacion:
            print(f"    Horario: {horario}, Salón: {salon}")

asignacion_horarios()


