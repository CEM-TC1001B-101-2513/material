# Convertir de calificación numérica a letra
# Mayor a 90 -> A
# Mayor a 80 y menor o igual a 90 -> B
# Mayor a 70 y menor o igual a 80 -> C
# Mayor a 60 y menor o igual a 70 -> D
# Menor o igual a 60 -> F
calificación = int(input("Ingresa tu calificación: "))
if calificación > 90:
    print("A")
if calificación > 80 and calificación <= 90:
    print("B")
if calificación > 70 and calificación <= 80:
    print("C")
if calificación > 60 and calificación <= 70:
    print("D")
if calificación <= 60:
    print("F")
#----------------------------------------
# Para que no revise todas las condiciones en todos los casos
if calificación > 90:
    print("A")
else:
    if calificación > 80:
        print("B")
    else:
        if calificación > 70:
            print("C")
        else:
            if calificación > 60:
                print("D")
            else:
                print("F")
                
# Versión con elif
if calificación > 90:
    print("A")
elif calificación > 80:
    print("B")
elif calificación > 70:
    print("C")
elif calificación > 60:
    print("D")
else:
    print("F")



