alumnos = ["Pedro", "María", "José", "Carlos", "Fernanda"]
nombre = input("Ingresa el nombre del alumno a buscar: ")
alumno_encontrado = False
for alumno in alumnos:
    if alumno == nombre:
        alumno_encontrado = True
# if alumno_encontrado == True
if alumno_encontrado:
    print(f"{nombre} está dentro de la lista.")
else:
    print(f"{nombre} no se encuentra en la lista.")

# -------------------------------------------------
for alumno in alumnos:
    if alumno == nombre:
        print(f"{nombre} está dentro de la lista.")
        break
else: # Si el ciclo se terminó de ejecutar sin un break
    print(f"{nombre} no se encuentra en la lista.")