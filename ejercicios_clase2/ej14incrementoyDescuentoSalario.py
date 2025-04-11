salario_actual = float(input("Ingrese el salario actual del empleado: "))

incremento = salario_actual * 0.08
salario_incremento = salario_actual + incremento

descuento = salario_incremento * 0.025
nuevo_salario = salario_incremento - descuento

print(f"Incremento: {incremento:.2f}")
print(f"Descuento: {descuento:.2f}")
print(f"El nuevo salario del empleado es: {nuevo_salario:.2f}")