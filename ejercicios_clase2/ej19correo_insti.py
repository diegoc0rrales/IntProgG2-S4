def quitar_acentos(texto):
    reemplazos = {
        "á": "a", "é": "e", "í": "i", "ó": "o", "ú": "u",
        "Á": "a", "É": "e", "Í": "i", "Ó": "o", "Ú": "u",
        "ñ": "n", "Ñ": "n"
    }
    for acento, sin_acento in reemplazos.items():
        texto = texto.replace(acento, sin_acento)
    return texto

nombre = input("Ingresa tu nombre: ").strip().lower()
apellido = input("Ingresa tu apellido: ").strip().lower()
universidad = input("Ingresa el nombre de tu universidad: ").strip().lower()

nombre = quitar_acentos(nombre)
apellido = quitar_acentos(apellido)
universidad = quitar_acentos(universidad)

universidad = universidad.replace(" ", "")

correo = f"{nombre}.{apellido}@{universidad}.edu.ni"

print(f"Tu correo institucional es: {correo}")
