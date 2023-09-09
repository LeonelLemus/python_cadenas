precio_euros = float(input("Introduce el precio del producto en euros, con dos decimales: "))
precio_centimos = int(precio_euros * 100)
euros = precio_centimos // 100
centimos = precio_centimos % 100

print(f"El precio de {precio_euros:.2f} euros equivale a {euros} euros y {centimos} céntimos.")