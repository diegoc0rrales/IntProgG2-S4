presupuesto_total = float(input("Ingresa el monto del presupuesto anual del hospital: "))

urgencias = presupuesto_total * 0.37
pediatria = presupuesto_total * 0.42
traumatologia = presupuesto_total * 0.21

print(f"Urgencias recibirá: C${urgencias:.2f}")
print(f"Pediatría recibirá: C${pediatria:.2f}")
print(f"Traumatología recibirá: C${traumatologia:.2f}")
