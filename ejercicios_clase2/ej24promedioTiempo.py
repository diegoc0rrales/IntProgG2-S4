lunes = float(input("Ingresa el tiempo del lunes (en minutos): "))
miercoles = float(input("Ingresa el tiempo del miércoles (en minutos): "))
viernes = float(input("Ingresa el tiempo del viernes (en minutos): "))

promedio = (lunes + miercoles + viernes) / 3

print(f"El tiempo promedio de la semana es: {promedio:.2f} minutos")
