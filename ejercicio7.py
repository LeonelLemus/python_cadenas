correo = input("Introduce tu correo electronico: ")
nombre, dominio = correo.split('@', 1)

nuevo_correo = f"{nombre}@ceu.es"

print("Nuevo correo con dominio ceu.es:", nuevo_correo)