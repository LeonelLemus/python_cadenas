frase = input("Introduzca una frase: ")
vocal = input("Introduzca una vocal: ")

if vocal.lower() in 'aeiou':
    frase_modificada = frase.replace(vocal.lower(), vocal.upper())

    print("Frase con la vocal en mayúscula:", frase_modificada)
else:
    print("Por favor, introduce una vocal válida (a, e, i, o, u).")