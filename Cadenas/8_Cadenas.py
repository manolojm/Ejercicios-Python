# 8_Cadenas

# 8. Escribe un programa que pinte por pantalla una pirámide
# rellena a base de asteriscos. La base de la pirámide debe
# estar formada por 9 asteriscos.

cadena = "*"

for i in range(0, 5):
    print(f'{cadena:^50}')
    cadena += "**"