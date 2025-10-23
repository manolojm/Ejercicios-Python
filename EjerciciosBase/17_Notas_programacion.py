# 17_Notas_programacion

nota1 = float(input('Introduzca la nota del primer examen: '))
nota2 = float(input('Introduzca la nota del segundo examen: '))

notaFinal = ((nota1 + nota2) / 2)

if notaFinal < 5:
    notaRecu = input('Cual ha sido el resultado de recuperacion? (apto / no apto) ')
    if notaRecu == 'apto':
        notaFinal = 5
        
print("La nota final es " , notaFinal)
    

    
