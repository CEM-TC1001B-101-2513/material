sueldo = float(input("Ingresa tu salario: "))
if sueldo <= 578.52:
    cuota = 0
    porcentaje = 0.0192
    límite_inferior = 0.01
elif sueldo <= 4910.18:
    cuota = 11.11
    porcentaje = 0.064
    límite_inferior = 578.53
isr = (sueldo - límite_inferior) * porcentaje + cuota
sueldo_neto = sueldo - isr
print(f"Tu sueldo neto es de: ${sueldo_neto:,.2f} después de descontar ${isr:,.2f} de ISR")