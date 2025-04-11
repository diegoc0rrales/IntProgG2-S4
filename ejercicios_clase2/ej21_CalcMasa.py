presion = float(input("Ingresa la presión: "))
volumen = float(input("Ingresa el volumen: "))
temperatura = float(input("Ingresa la temperatura (en grados Fahrenheit): "))

masa = (presion * volumen) / (0.37 * (temperatura + 460))

print(f"La masa calculada es: {masa:.2f}")
