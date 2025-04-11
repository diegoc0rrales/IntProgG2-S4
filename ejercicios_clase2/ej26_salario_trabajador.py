nombre = input("Ingresa el nombre del trabajador: ")
horas_trabajadas = float(input("Ingresa la cantidad de horas trabajadas: "))
precio_por_hora = float(input("Ingresa el precio que cobra por hora: "))

sueldo_bruto = horas_trabajadas * precio_por_hora

descuento = sueldo_bruto * 0.05

salario_neto = sueldo_bruto - descuento

print("\n--- Detalle del salario ---")
print(f"Nombre del trabajador: {nombre}")
print(f"Sueldo bruto: C${sueldo_bruto:.2f}")
print(f"Descuento por renta (5%): C${descuento:.2f}")
print(f"Salario a pagar: C${salario_neto:.2f}")