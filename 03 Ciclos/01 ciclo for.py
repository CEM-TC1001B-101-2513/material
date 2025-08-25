# for -> Sólo sirve para ciclos definidos
# Usa una variable para recorrer una secuencia

# range(final) -> Secuencia de números que inicia en 0,
# avanza de 1 en 1 y termina antes de final
for i in range(5):
    print(f"El valor de i es: {i}")
print("-" * 30)

# range(inicio, final) -> Secuencia de números que inicia en inicio
# avanza de 1 en 1 y termina antes de final
for i in range(5,10):
    print(f"El valor de i es: {i}")
print("-" * 30)

# range(inicio, final, paso) -> Secuencia de números que inicia en
# inicio, avanza de paso en paso y termina antes de final
for i in range(4, 15, 3):
    print(f"El valor de i es: {i}")
print("-" * 30)
    
texto = "hola mundo"
for i in texto:
    print(f"El valor de i es: {i}")
print("-" * 30)

lista = [145.82, 5, True, "hola", [1,2,3]]
for i in lista:
    print(f"El valor de i es: {i}")


