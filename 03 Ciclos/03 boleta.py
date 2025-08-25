num_materias = int(input("Ingresa la cantidad de materias que cursaste: "))
promedio = 0
for i in range(1,num_materias+1):
    materia = float(input(f"Ingresa la calificación de tu materia {i}: "))
    #promedio = promedio + materia
    promedio += materia
#promedio = promedio / num_materias
promedio /= num_materias
print(f"El promedio de tu semestre fue: {promedio:,.2f}")