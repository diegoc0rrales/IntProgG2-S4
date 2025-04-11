precio1 = float(input("Ingrese el precio del primer producto: "))
precio2 = float(input("Ingrese el precio del segundo producto: "))
precio3 = float(input("Ingrese el precio del tercer producto: "))

subtotal = precio1 + precio2 + precio3

iva = subtotal * 0.15

total = subtotal + iva

print(f"\nSubtotal: {subtotal:.2f}")
print(f"IVA (15%): {iva:.2f}")
print(f"Total a pagar: {total:.2f}")