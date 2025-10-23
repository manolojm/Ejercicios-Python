# 12_Ecuacion_de_primer_grado

terminoA = float(input('Introduzca el primer termino: '))
terminoB = float(input('Introduzca el segundo termino: '))
terminoC = float(input('Introduzca el tercer termino: '))

if terminoA != 0:
    resultado = (terminoC - terminoB) / terminoA
    print("X = " , resultado)
else:
    print("Error al introducir los terminos")