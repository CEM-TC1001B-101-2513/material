# Parámetros -> Datos que necesita mi función
# Valor de retorno -> Resultado de mi función

# Sin parámetros y sin valor de retorno
def suma1():
    x = float(input("Ingresa el valor de x: "))
    y = float(input("Ingresa el valor de y: "))
    resultado = x + y
    print(f"El resultado de la suma es: {resultado}")

#suma1()
#print(resultado)
    
# Con parámetros y sin valor de retorno
def suma2(x, y):
    resultado = x + y
    print(f"El resultado de la suma es {resultado}")

#suma2(50, 30)
#a = float(input("Ingresa el valor 1: "))
#b = float(input("Ingresa el valor 2: "))
#suma2(a, b)

# Con parámetros y con valor de retorno
def suma3(x, y):
    resultado = x + y
    return resultado
# Argumentos posicionales
res = suma3(45, 85) + 10 / 2
print(f"El resultado es: {res}")
# Argumentos por palabra clave (keyword)
res = suma3(y = 15, x = 30)
print(f"El resultado es: {res}")
