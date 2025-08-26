import random
seguir_jugando = 1
while seguir_jugando == 1:
    aleatorio = random.randint(1,100)
    número = 0
    intentos = 0
    while número != aleatorio:
        número = int(input("Intenta adivinar el número entre 1 y 100: "))
        if número > aleatorio:
            print("El número que buscas es más pequeño.")
        elif número < aleatorio:
            print("El número que buscas es más grande.")
        intentos += 1
    print(f"Adivinaste, el número era {aleatorio}. Te tomó {intentos} intentos.")
    seguir_jugando = int(input("¿Desea seguir jugando? 1)Sí, 2)No: "))