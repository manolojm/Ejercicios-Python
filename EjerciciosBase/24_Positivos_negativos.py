# 24_Positivos_negativos
positivos = 0
negativos = 0

for i in range(0, 10):
    numero = float(input(f"Introduzca un numero ({i+1}/10): "))
    
    if numero < 0:
        negativos += 1
    else:
        positivos +=1
        
print(f"Se han introducido {positivos} numeros positivos")
print(f"Se han introducido {negativos} numeros negativos")