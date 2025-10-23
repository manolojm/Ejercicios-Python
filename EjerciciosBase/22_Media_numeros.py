# 22_Media_numeros

sumatoria = 0;
contador_numeros = 0;

nuevo_numero = int(input('Introduzca nuevo numero (negativo para acabar): '))
if nuevo_numero > 0:
    sumatoria += nuevo_numero
    contador_numeros += 1
    
    while nuevo_numero > 0:
        nuevo_numero = int(input('Introduzca otro numero (negativo para acabar): '))
        if nuevo_numero > 0:
            sumatoria += nuevo_numero
            contador_numeros += 1
        
if contador_numeros > 0:
    media = sumatoria / contador_numeros

print(f"La media de sus numeros es {media}")
        