# 9_Cadenas

cadena = "*"
numero_espacios = 1
numero_asteriscos = 1

for i in range(0, 5):
    if i == 0 or i == 4:
        print(f'{cadena * numero_asteriscos:^50}')
    else:
        print(f'{cadena + " " * numero_espacios + cadena:^50}')
        numero_espacios += 2;
        
    numero_asteriscos += 2
    