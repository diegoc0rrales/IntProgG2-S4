a = float(input("Ingresa el valor de la primera variable (a): "))
b = float(input("Ingresa el valor de la segunda variable (b): "))

print(f"Antes del intercambio: a = {a}, b = {b}")

aux = a
a = b
b = aux

# Mostrar los valores después del intercambio
print(f"Después del intercambio: a = {a}, b = {b}")
