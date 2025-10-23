# 7_Calcular_nota

nota1 = float(input('Introduzca la nota que ha obtenido en el primer examen: '))
notaF = float(input('Introduzca la nota que desea obtener en la evaluacion: '))
nota2 = round((notaF - nota1 * 0.4) / 0.6, 2)
print(f"Ha de sacar un {nota2} en el siguiente examen")