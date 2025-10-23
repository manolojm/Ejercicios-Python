## 14_Horoscopo

dia = int(input('Introduzca dia de nacimiento: '))
mes = int(input('Introduzca mes de nacimiento: '))

if (mes == 3 and dia >= 21) or (mes == 4 and dia <= 19):
    resultado = "Aries"
elif (mes == 4 and dia >= 20) or (mes == 5 and dia <= 20):
    resultado = "Tauro"
elif (mes == 5 and dia >= 21) or (mes == 6 and dia <= 20):
    resultado = "Geminis"
elif (mes == 6 and dia >= 21) or (mes == 7 and dia <= 22):
    resultado = "Cancer"
elif (mes == 7 and dia >= 23) or (mes == 8 and dia <= 22):
    resultado = "Leo"
elif (mes == 8 and dia >= 23) or (mes == 9 and dia <= 22):
    resultado = "Virgo"
elif (mes == 9 and dia >= 23) or (mes == 10 and dia <= 22):
    resultado = "Libra"
elif (mes == 10 and dia >= 23) or (mes == 11 and dia <= 21):
    resultado = "Escorpio"
elif (mes == 11 and dia >= 22) or (mes == 12 and dia <= 21):
    resultado = "Sagitario"
elif (mes == 12 and dia >= 22) or (mes == 1 and dia <= 19):
    resultado = "Capricornio"
elif (mes == 1 and dia >= 20) or (mes == 2 and dia <= 18):
    resultado = "Acuario"
elif (mes == 2 and dia >= 19) or (mes == 3 and dia <= 20):
    resultado = "Piscis"
else:
    resultado = "Datos incorrectos"
                        
print(resultado)       