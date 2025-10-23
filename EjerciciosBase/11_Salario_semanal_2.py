# 11_Salario_semanal_2

horas = int(input('Introduzca el numero de horas trabajadas: '))

if horas <= 40:
    resultado = horas * 12
else:
    resultado = (40 * 12) + ((horas-40)*16)
    
print(f"Ha ganado un total de {resultado} euros");