compras = input("Introduce los productos de la cesta de la compra separados por comas: ")
productos = compras.split(',')

for producto in productos:
    print(producto.strip())
