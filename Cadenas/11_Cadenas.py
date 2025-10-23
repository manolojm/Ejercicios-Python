# 11_Cadenas

# 11. Escribe un programa que calcule el precio final de
# un producto según varias cosas.

# Entrada de datos
base = float(input("Introduzca la base imponible: "))
tipo_iva = input("Introduzca el tipo de IVA (general, reducido o superreducido): ")
tipo_descuento = input("Introduzca el codigo promocional (nopro, mitad, meno5 o 5porc): ")

# Calculo IVA
if tipo_iva == "reducido":
    porciento_iva = 10
elif tipo_iva == "superreducido":
    porciento_iva = 4
else:
    porciento_iva = 21

# Total con IVA
total_iva = base * porciento_iva / 100
total_con_iva = base + total_iva 
    
# Calculo descuento
if tipo_descuento == "mitad":
    total_descuento = 0.0 - total_con_iva / 2
elif tipo_descuento == "meno5":
    total_descuento = 0.0 - 5
elif tipo_descuento == "5porc":
    total_descuento = 0.0 - total_con_iva * 5 / 100
else:
    total_descuento = 0.0

# Total final
total_final = total_con_iva + total_descuento

# Resultados por pantalla
print(f"\n{'Base imponible':<25} {base:>7}")
print(f"{'IVA (' + str(porciento_iva) + '%)':<25} {total_iva:>7}")
print(f"{'Precio con IVA':<25} {total_con_iva:>7}")
print(f"{'Cód. promo. (' + tipo_descuento + '):':<25} {total_descuento:>7}")
print(f"{'TOTAL':<25} {total_final:>7}")