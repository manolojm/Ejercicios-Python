# 13_Cadenas

# 13. La tienda online BanderaDeEspaña.es vende banderas personalizadas
# de la máxima calidad y nos ha pedido hacer un configurador que calcule
# el precio según el alto y el ancho.

# Entrada de datos
altura = float(input("Introduzca la altura de la bandera en cm: "))
anchura = float(input("Ahora introduzca la anchura: "))
tiene_escudo = input("¿Quiere escudo bordado? (s/n): ")

# Calculos
area = altura * anchura
precio_area = area / 100
gastos_de_envio = 3.25

# Escudo
if tiene_escudo == "s":
    precio_escudo = 2.50
else:
    precio_escudo = 0.00

# Precio total
precio_total = precio_area + precio_escudo + gastos_de_envio

# Resultados por pantalla
print("\nGracias. Aquí tiene el desglose de su compra.")
print(f"{'Bandera de ' + str(area) + ' cm2:':<25} {precio_area:>5} €")
print(f"{'Con escudo: ' if tiene_escudo == 's' else 'Sin escudo: ':<25} {precio_escudo:>5} €")
print(f"{'Gastos de envío:':<25} {gastos_de_envio:>5} €")
print(f"{'Total:':<25} {precio_total:>5} €")