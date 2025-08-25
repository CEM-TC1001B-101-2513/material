edad = int(input("Indica tu edad: "))

if edad >= 18:
    if edad >= 60:
        print("Puedes tramitar tu INAPAM")
    else:
        print("Eres mayor de edad")
else:
    faltante = 18 - edad
    print(f"Te faltan {faltante} años para ser mayor de edad.")