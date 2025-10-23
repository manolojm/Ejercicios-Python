# 25_Numeros

contador_numeros = 0;
media_impares = 0.0;
suma_impares = 0.0;
numero_impares = 0;
par_mayor = 0.0;

numero = float(input("Introduzca un numero (negativo para acabar)"))
if numero > 0:
    
    contador_numeros += 1
    if (numero % 2 != 0):
        suma_impares += numero
        numero_impares += 1
    if (numero % 2 == 0 and numero > par_mayor):
        par_mayor = numero
        
    while numero > 0:
        numero = float(input("Introduzca otro numero (negativo para acabar)"))
        
        if numero > 0:
            contador_numeros += 1
            if (numero % 2 != 0):
                suma_impares += numero
                numero_impares += 1
            if (numero % 2 == 0 and numero > par_mayor):
                par_mayor = numero
            
if numero_impares > 0:
    media_impares = suma_impares / numero_impares
    
print(f'Se han introducido {contador_numeros} numeros')
print(f'La media de los numeros impares es: {media_impares}')
print(f'El mayor de los numeros pares es {par_mayor}')
