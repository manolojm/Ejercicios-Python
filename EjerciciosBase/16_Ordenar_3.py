# 16_Ordenar_3

numero1 = int(input('Introduzca un primer numero: '))
numero2 = int(input('Introduzca un segundo numero: '))
numero3 = int(input('Introduzca un tercer numero: '))

if (numero1 > numero2 and numero1 > numero3 and numero2 > numero3):
    print(f"{numero1} > {numero2} > {numero3}")
elif (numero1 > numero2 and numero1 > numero3 and numero3 > numero2):
    print(f"{numero1} > {numero3} > {numero2}")
elif (numero2 > numero1 and numero2 > numero3 and numero1 > numero3):
    print(f"{numero2} > {numero1} > {numero3}")
elif (numero2 > numero1 and numero2 > numero3 and numero3 > numero1):
    print(f"{numero2} > {numero3} > {numero1}")
elif (numero3 > numero1 and numero3 > numero2 and numero1 > numero2):
    print(f"{numero3} > {numero1} > {numero2}")
else:
    print(f"{numero3} > {numero2} > {numero1}")