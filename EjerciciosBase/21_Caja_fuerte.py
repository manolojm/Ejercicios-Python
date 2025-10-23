# 21_Caja_fuerte

mensaje = '';
numero_caja = 1234;
numero_elegido = 0;
intentos = 4;

numero_elegido = int(input('Introduzca numero de cuatro cifras: '))
if numero_elegido == numero_caja:
    print("La caja fuerte se ha abierto")
else:
    intentos -= 1;
    print("Lo siento, esa no es la combinacion")
    print(f"Le quedan {intentos} intentos")
    
    while intentos > 0 and numero_elegido != numero_caja:
        numero_elegido = int(input('Introduzca numero de cuatro cifras: '))
        if numero_elegido == numero_caja:
            print("La caja fuerte se ha abierto")
        else:
            intentos -= 1;
            print("Lo siento, esa no es la combinacion")
            print(f"Le quedan {intentos} intentos")
            
