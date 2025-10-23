# 18_Cadenas

# 18. Realiza un programa que pinte una X hecha de asteriscos.
# El programa debe pedir la altura. Se debe comprobar que la
# altura sea un número impar mayor o igual a 3, en caso
# contrario se debe mostrar un mensaje de error.

n = int(input("Introduzca la altura de la u: "))
print()

cadena = "*"

for i in range(-(int(n/2)), int(n/2)+1):
    if i == 0:
        print(f'{cadena:^50}')
    else:
        print(f'{cadena + (" "*(abs(i)*2-1)) + cadena:^50}')
    
# 1 * 2 - 1 = 1
# 2 * 2 - 1 = 3
# 3 * 2 - 1 = 5...