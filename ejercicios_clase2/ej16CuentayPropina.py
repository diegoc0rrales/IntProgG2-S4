total_cuenta = float(input("Ingrese el total de la cuenta: "))
porcentaje_propina = float(input("Ingrese el porcentaje de propina (%): "))

propina = total_cuenta * (porcentaje_propina / 100)

print(f"La propina a dejar es: {propina:.2f}")