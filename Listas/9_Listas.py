# 9_Listas
import random
import Min_max

def mostrar_mesas():
    print("\n- - - - - - - - - -")
    #print("Las mesas están configuradas")
    print("Mesas: ")
    for i in range(10):
        print(f"{str(i+1) + ' | ':<5}", end='')
     
    print("\nOcupación: ")
    for i in range(10):
        print(f"{str(vector_mesas[i]) + ' | ':<5}", end='')
    print("\n- - - - - - - - - -")
    
vector_mesas = []
for i in range(10):
    nuevo_numero = (random.randint(0, 4))
    vector_mesas.append(nuevo_numero)
    
mostrar_mesas()

mi_mensaje = "\n¿Cuántos son? Introduzca -1 para salir del programa: "
mi_error = "Lo siento, no admitimos grupos tan grandes, haga grupos de 4 personas como máximo e intente de nuevo"

num_mesa_libre = 0
mesas_libres = vector_mesas.count(num_mesa_libre)

# Buscamos las mesas libres con cero comensales
if mesas_libres > 0:
    for i in range(mesas_libres):
        nuevo_comensal = Min_max.leer_entero_min_max(minimo = -1, maximo = 4, mensaje=mi_mensaje, error=mi_error)
        
        encontrada = vector_mesas.index(num_mesa_libre)
        if nuevo_comensal > 0:
            lugar = vector_mesas.index(num_mesa_libre)
            vector_mesas.remove(num_mesa_libre)
            vector_mesas.insert(lugar, nuevo_comensal)
            print(f"\nPor favor, siéntese en la mesa número {lugar+1}.")
            mostrar_mesas()
        else:
            break;

# Buscamos el resto de mesas donde quedan los comensales sin romper el grupo
while True:
    nuevo_comensal = Min_max.leer_entero_min_max(minimo = -1, maximo = 4, mensaje=mi_mensaje, error=mi_error)
    num_mesa_libre = 4 - nuevo_comensal + 1

    vector_numeros_mesas_libres = []
    vector_mesas_libres = []
    for i in range(num_mesa_libre):
        vector_numeros_mesas_libres.append(i)

    for i in vector_mesas:
        if i in vector_numeros_mesas_libres:
            vector_mesas_libres.append(i)
            
    if len(vector_mesas_libres) > 0:

        encontrada = vector_mesas.index(vector_mesas_libres[0])
        
        lugar = vector_mesas.index(vector_mesas_libres[0])
        nuevo_numero_comensales = vector_mesas[lugar] + (4 - vector_mesas_libres[0])
        
        vector_mesas.remove(vector_mesas_libres[0])
        vector_mesas.insert(lugar, nuevo_numero_comensales)
        print(f"\nPor favor, siéntese en la mesa número {lugar+1}.")
        mostrar_mesas()
    else:
        print(f"\nLo sentimos, no nos quedan mesas libres.")
        break;