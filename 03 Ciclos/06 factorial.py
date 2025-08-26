# Factorial
n = int(input("Ingrese el valor de n: "))
factorial = 1
for i in range(1, n+1):
    #factorial = factorial * i
    factorial *= i
print(f"El factorial de {n} es: {factorial}")
# ------------------------------------
factorial = 1
i = 1
while i <= n:
    factorial *= i
    i += 1
print(f"El factorial de {n} es: {factorial}")