telefono = input("Por favor, introduce un número de teléfono con el formato +34-XXXXXXXXX-XX: ")

if telefono.startswith("+34-") and len(telefono) == 15 and telefono[9] == "-" and telefono[12:].isdigit():

    numero_sin_prefijo_y_extension = telefono[4:12]
    
    print("Número de teléfono sin prefijo ni extensión:", numero_sin_prefijo_y_extension)
else:
    print("El número de teléfono no tiene el formato válido.")
