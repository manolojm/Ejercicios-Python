# 15_Cadenas

# 15. Una pastelería nos ha pedido realizar un programa
# que haga presupuestos de tartas.

# Entrada de datos
opcion_sabor = input("Elija un sabor (manzana, fresa o chocolate): ")
if opcion_sabor == "chocolate":
    opcion_chocolate = input("¿Qué tipo de chocolate quiere? (negro o blanco): ")
else:
    opcion_chocolate = ""
opcion_nata = input("¿Quiere nata? (si o no): ")
opcion_nombre = input("¿Quiere ponerle un nombre? (si o no): ")

# Precio base
if opcion_sabor == "manzana":
    precio_base = 18.00
elif opcion_sabor == "fresa":
    precio_base = 16.00
else:
    if opcion_chocolate == "negro":
        precio_base = 14.00
    elif opcion_chocolate == "blanco":
        precio_base = 15.00
    else:
        precio_base = 0.00

# Nata
if opcion_nata == "si":
    dlc_nata = 2.50
else:
    dlc_nata = 0.00
    
# Nombre  
if opcion_nombre == "si":
    dlc_nombre = 2.75
else:
    dlc_nombre = 0.00

# Precio total
precio_total = precio_base + dlc_nata + dlc_nombre

# Resultados por pantalla
print(f'\nTarta de {opcion_sabor}{" "+opcion_chocolate+":" if opcion_chocolate != "" else ":"} {precio_base} €')

if opcion_nata == "si":
    print(f'Con nata: {dlc_nata} €')

if opcion_nombre == "si":
    print(f'Con nombre: {dlc_nombre} €')
    
print(f'Total: {precio_total} €')