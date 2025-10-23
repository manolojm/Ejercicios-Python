# 18_Piedra_papel_tijera
jugador1 = input('Jugador uno saca: ')
jugador2 = input('Jugador dos saca: ')

if jugador1 == 'piedra' and jugador2 == 'piedra':
    resultado = "Empate"
elif jugador1 == 'piedra' and jugador2 == 'tijera':
    resultado = "Jugador 1 gana"
elif jugador1 == 'piedra' and jugador2 == 'papel':
    resultado = "Jugador 2 gana"
elif jugador1 == 'papel' and jugador2 == 'papel':
    resultado = "Empate"
elif jugador1 == 'papel' and jugador2 == 'piedra':
    resultado = "Jugador 1 gana"
elif jugador1 == 'papel' and jugador2 == 'tijera':
    resultado = "Jugador 2 gana"
elif jugador1 == 'tijera' and jugador2 == 'tijera':
    resultado = "Empate"
elif jugador1 == 'tijera' and jugador2 == 'papel':
    resultado = "Jugador 1 gana"
elif jugador1 == 'tijera' and jugador2 == 'piedra':
    resultado = "Jugador 2 gana"
else:
    resultado = "Entrada invalida"
    
print(resultado)
