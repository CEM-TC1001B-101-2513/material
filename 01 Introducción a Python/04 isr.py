salario_bruto = float(input("Ingresa tu salario bruto: "))

isr = salario_bruto * 0.2136
salario_neto = salario_bruto - isr

print(f"El ISR descontado es de: ${isr:,.2f}")
print(f"El salario neto es: ${salario_neto:,.2f}")