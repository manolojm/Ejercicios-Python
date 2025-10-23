# Leer entero
def leer_numero_entero(mensaje="Introduce un número: ", error="No se introdujo un número"):
    """
    Prueba
    """
    
    while(True):
        try:
            numero = int(input(mensaje))
            break;
        except ValueError:
            print(error)
    return numero

# Leer entero mínimo
def leer_entero_minimo(minimo = 0, mensaje="Introduce un número: ", error="No se introdujo un número"):
    """
    Prueba
    """
    
    #numero = leer_numero_entero(mensaje, error)
    #while(numero < minimo):
    #    numero = leer_numero_entero(mensaje, error)
    #return numero

    while(numero := leer_numero_entero(mensaje, error) < minimo):
        pass
    return numero
    
            
# Leer entero máximo
def leer_entero_maximo(maximo = 4, mensaje="Introduce un numero: ", error="No se introdujo un número"):
    while((numero := leer_numero_entero(mensaje, error)) > maximo):
        pass
    return numero

# Leer entero entre mínimo y máximo
def leer_entero_min_max(minimo = 0, maximo = 10, mensaje="Introduce un número: ", error="Número no válido"):
    numero = leer_numero_entero(mensaje, error)

    while(numero < minimo or numero > maximo):
        numero = leer_numero_entero(mensaje, error)
        print(error)
    return numero
#numero = leer_entero_min_max(minimo = 1, maximo = 4, mensaje="Introduzca un número entero: ")