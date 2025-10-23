# 14_Cadenas

# 14. Realiza un programa que calcule el precio de unas entradas de
# cine en función del número de personas y del día de la semana.

# Entrada de datos
print("Venta de entradas CineCampa")
numero_entradas = int(input("Número de entradas: "))
dia_semana = input("Día de la semana: ")
tiene_tarjeta = input("¿Tiene tarjeta CineCama? (s/n): ")

# Dia de la semana
if dia_semana == "miercoles":
    precio_individual = 5.00
    precio_entradas = numero_entradas * precio_individual
elif dia_semana == "jueves":
    precio_individual = 8.00
    precio_pareja = 11.00
    precio_entradas = (numero_entradas // 2) * precio_pareja + (numero_entradas % 2) * precio_individual
else:
    precio_individual = 8.00
    precio_entradas = numero_entradas * precio_individual

# Tarjeta descuentos
if tiene_tarjeta == "s":
    descuento = precio_entradas * 10 / 100
else:
    descuento = 0.00

# Precio final
precio_entradas_final = precio_entradas - descuento

# Resultados por pantalla
print("\nAquí tiene sus entradas. Gracias por la compra")

if dia_semana != "jueves":
    print(f'{"Entradas individuales:":<35} {numero_entradas:^5}')
    print(f'{"Precio por entrada individual:":<35} {precio_individual:>5} €')
else:
    if numero_entradas % 2 != 0:
        print(f'{"Entradas individuales:":<35} {numero_entradas % 2:^5}')
        print(f'{"Precio por entrada individual:":<35} {precio_individual:>5} €')
    print(f'{"Entradas de parejas:":<35} {numero_entradas//2:^5}')
    print(f'{"Precio por entrada de pareja:":<35} {precio_pareja:>5} €')
    
print(f'{"Total":<35} {precio_entradas:>5} €')
print(f'{"Descuento":<35} {descuento:>5} €')
print(f'{"A pagar":<35} {precio_entradas_final:>5} €')