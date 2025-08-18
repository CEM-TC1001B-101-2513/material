materia1 = float(input("Ingresa la calificación de tu materia 1: "))
materia2 = float(input("Ingresa la calificación de tu materia 2: "))
materia3 = float(input("Ingresa la calificación de tu materia 3: "))
materia4 = float(input("Ingresa la calificación de tu materia 4: "))
materia5 = float(input("Ingresa la calificación de tu materia 5: "))
materia6 = float(input("Ingresa la calificación de tu materia 6: "))
materia7 = float(input("Ingresa la calificación de tu materia 7: "))
promedio = (materia1 + materia2 + 
            materia3 + materia4 + \
            materia5 + materia6 + materia7) / 7

# Opción que utilizaremos en el curso
# f-strings
# f"{}" -> Indica a Python que debe evaluar lo que está dentro
# de las llaves e incluirlo en el texto
# : -> Debe aplicar un formato especial
# , -> Incluir separador de miles
# .n -> Redondear a n decimales
# f -> Aparecer como float en lugar de formato científico
print(f"El promedio de tu semestre fue: {promedio:,.2f}")

# Maneras antiguas de presentar texto
print("El promedio de tu semestre fue:", promedio)
print("El promedio de tu semestre fue: " + str(promedio))
print("El promedio de tu semestre fue: {0:,.2f}".format(promedio))
