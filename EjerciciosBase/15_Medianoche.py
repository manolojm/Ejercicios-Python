# 15_Medianoche

horas = int(input('Introduzca numero de horas: '))
minutos = int(input('Introduzca numero de minutos: '))
segundosMedianoche = 24 * 60 * 60;

if (horas < 24 and minutos < 60) or (horas <= 24 and minutos == 0):
    resultado = segundosMedianoche - (horas*60*60) - (minutos*60);
    print(f"Quedan {resultado} segundos hasta la medianoche")
else:
    print("Datos errones")
