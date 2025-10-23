# 12_Cadenas

# 12. Escribe un programa que genere la nómina (bien desglosada) de un
# empleado según las siguientes condiciones

# Entrada de datos
print("1 - Programador junior")
print("2 - Prog. senior")
print("3 - Jefe de proyecto")

cargo = int(input("Introduzca el cargo del empleado (1 - 3): "))
dias_viaje = int(input("¿Cuántos días ha estado de viaje visitando clientes? "))
estado_civil = int(input("Introduzca su estado civil (1 - Soltero, 2 - Casado): "))

# Sueldo base
if cargo == 3:
    sueldo_base = 1600.00
elif cargo == 2:
    sueldo_base = 1200.00
else:
    sueldo_base = 950.00

# Sueldo bruto
total_dietas = dias_viaje * 30
sueldo_bruto = sueldo_base + total_dietas

# IRPF
if estado_civil == 2:
    irpf = 20
else:
    irpf = 25
    
# Sueldo neto
retencion_irpf = sueldo_bruto * irpf / 100
sueldo_neto = sueldo_bruto - retencion_irpf

# Resultados por pantalla
print(f'\n{"":-^40}')
print(f"{'| Sueldo base':<25} {sueldo_base:>12} |")
print(f"{'| Dietas (' + str(dias_viaje) + ' viaje/s)':<25} {total_dietas:>12} |")

print(f'{"":-^40}')
print(f"{'| Sueldo bruto':<25} {sueldo_bruto:>12} |")
print(f"{'| Retención IRPF (' + str(irpf) + '%)':<25} {retencion_irpf:>12} |")

print(f'{"":-^40}')
print(f"{'| Sueldo neto':<25} {sueldo_neto:>12} |")

print(f'{"":-^40}')


