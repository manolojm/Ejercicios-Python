# 10_Saludo

hora = int(input('Introduzca una hora: '))

if hora >= 6 and hora <= 12:
    resultado = "Buenos dias"
elif hora >= 13 and hora <= 20:
    resultado = "Buenas tardes"
elif (hora >= 21 and hora <= 23) or (hora >= 0 and hora <= 5):
    resultado = "Buenas noches"
else:
    resultado = "Hora incorrecta"
    
print(resultado)