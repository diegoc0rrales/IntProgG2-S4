#adivinar un número
import random
numero_secreto= random.randint(1,10)


while(True):
    numero_usuario=int(input("Dime un número del 1 al 10: "))
    if (numero_usuario==numero_secreto):
        print(f"¡Has acertado el número secreto!: {numero_secreto}")
        break
    else:
        print("Has fallado, inténtalo de nuevo")
    if(numero_usuario>numero_secreto):
        print("El número secreto es menor que el que has introducido")
    else:
        print("El número secreto es mayor que el que has introducido")