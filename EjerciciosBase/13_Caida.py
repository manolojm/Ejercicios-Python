# 13_Caida
import math

altura = float(input('Introduzca la altura: '))
gravedad = 9.81;

if altura > 0:
    resultado = round(math.sqrt((2 * altura) / gravedad), 2);
    print('Tiempo que tardara en caer = ' , resultado , ' segundos')
else:
    print("Error al introducir los datos")