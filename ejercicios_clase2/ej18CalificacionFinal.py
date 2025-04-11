tareas = float(input("Ingresa la calificación de tareas (sobre 100): "))
examen_parcial = float(input("Ingresa la calificación del examen parcial (sobre 100): "))
examen_final = float(input("Ingresa la calificación del examen final (sobre 100): "))

calificacion_final = (tareas * 0.30) + (examen_parcial * 0.30) + (examen_final * 0.40)

print(f"La calificación final del estudiante es: {calificacion_final:.2f}")