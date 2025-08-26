
precio_producto = 0
cuenta = 0
while precio_producto >= 0:
    cuenta += precio_producto
    precio_producto = float(input("Ingresa el precio del producto: "))
print(f"El total a pagar es de: ${cuenta:,.2f}")