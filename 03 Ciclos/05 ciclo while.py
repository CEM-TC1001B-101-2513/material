# Ciclo while
# La ejecución del ciclo depende completamente de nosotros
# Usualmente se usa una variable de control que se establece
# antes del ciclo, se usa dentro de la condición de paro y
# se debe modificar dentro del ciclo

#for i in range(1,11):
#    print(f"El valor de i es: {i}")

i = 1 # inicio
while i <= 10: # final
    print(f"El valor de i es: {i}")
    # i = i + 1
    i += 1 # paso
print("-" * 30)
# ---------------------------------

#lista = [1, 2, True, "hola"]
#for i in lista:
#    print(f"El valor de i es: {i}")

lista = [90, 2, True, "hola"]
# Se puede acceder a un elemento de la lista usando su posición
# Empezando de izquierda a derecha, la primera posición es 0
print(lista[2])
print(len(lista)) # length -> ¿Cuántos elementos hay dentro?

i = 0
while i < len(lista):
    print(f"lista[{i}] = {lista[i]}")
    i = i + 1
    #i += 1

print("-"*30)

# Ejemplo de un ciclo indefinido

continuar = 1
while continuar == 1:
    print("Ejecutando...")
    continuar = int(input("¿Desea seguir repitiendo? 1)Sí, 2)No: "))

print("-"*30)
# -----------------------------------

decisión = int(input("¿Desea compartir sus datos? 1)Sí, 2)No: "))
#while decisión != 1 and decisión != 2:
while decisión not in [1,2]:
    print("Error, debe elegir entre 1 para sí y 2 para no")
    decisión = int(input("¿Desea compartir sus datos? 1)Sí, 2)No: "))





