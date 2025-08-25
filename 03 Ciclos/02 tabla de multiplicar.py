# Tabla de multiplicar de un número
# Permitir el ingreso de un número entero n e imprimir
# su tabla de multiplicar del 1 al 10 con el formato:
# Si n vale 3:
# 3 x 1 = 3
# 3 x 2 = 6
# ...
# 3 x 10 = 30

n = int(input("Ingrese el valor de n: "))
for i in range(1, 11):
    resultado = n * i
    print(f"{n} x {i} = {resultado}")


