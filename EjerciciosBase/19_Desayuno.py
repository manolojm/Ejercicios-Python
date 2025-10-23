# 19_Desayuno

precio_churros = 1.5
precio_donuts = 1.0
precio_tostada_basica = 1.2
precio_tostada_especial = 1.6
precio_zumo = 1.8
precio_cafe = 1.2
precio_total = 0.0

opcion1 = input('Que ha tomado para comer? (tostada, churros o donuts) ')

if opcion1 == "churros":
    precio_total += precio_churros
elif opcion1 == "donuts":
    precio_total += precio_donuts
elif opcion1 == "tostada":
    opcion2 = input('La tostada es basica o especial? ')
    if opcion2 == "basica":
        precio_total += precio_tostada_basica
    elif opcion2 == "especial":
        precio_total += precio_tostada_especial
    else:
        print("Opcion erronea")
else:
    print("Opcion erronea")
        
opcion3 = input('Que ha tomado para beber? (zumo o cafe): ')
if opcion3 == "zumo":
    precio_total += precio_zumo
elif opcion3 == "cafe":
    precio_total += precio_cafe
else:
    print("Opcion erronea")
    
print(f"Su cuenta son {precio_total} euros")
    

