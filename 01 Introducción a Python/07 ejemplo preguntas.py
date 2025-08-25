# .strip() -> Quita los espacios del inicio y del final
# .lower() -> Convierte todo a minúsculas
# .upper() -> Convierte todo a mayúsculas
#respuesta = input("¿Actúas ética e irreprochablemente en tu trabajo? Sí/No: ").strip().lower()
#if respuesta == "sí" or respuesta == "si":
#    print("Respondió sí...")
conteo_sí = 0
respuesta = int(input("¿Actúas ética e irreprochablemente en tu trabajo? 1)Sí 2)No: "))
if respuesta == 1:
    #conteo_sí = conteo_sí + 1
    conteo_sí += 1
respuesta = int(input("¿Tu honradez y sinceridad proporcionan confianza a las demás personas de tu entorno laboral? 1)Sí 2)No: "))
if respuesta == 1:
    conteo_sí = conteo_sí + 1
print(conteo_sí)
