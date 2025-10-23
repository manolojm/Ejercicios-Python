# 6_Cadenas

# 6. Pide una cadena y dos caracteres por teclado (valida
# que sea un carácter), sustituye la aparición del primer
# carácter en la cadena por el segundo carácter.

cadena_1 = input("Introduzca una cadena: ")
cadena_2 = ""
caracter_1 = input("Introduzca un caracter: ")
caracter_2 = input("Introduzca otro caracter: ")

cadena_2 = cadena_1.replace(caracter_1, caracter_2)
print(cadena_2)