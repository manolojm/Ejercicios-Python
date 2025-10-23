# 4_Listas

# Variables
vector_nombres = []
vector_edades = []
vector_mayores_edad = []
vector_los_mayores = []
edad_mayor = 0

# Función para introducir la edad
def introducir_nueva_edad():
    edad_mayor = 0
    
    nueva_edad = int(input("Introduzca edad alumno: "))
    vector_nombres.append(nuevo_nombre)
    vector_edades.append(nueva_edad)
    
    # Mayores de edad
    if nueva_edad > 17:
        vector_mayores_edad.append(nuevo_nombre)
    
    # Edades mayores
    if nueva_edad == edad_mayor:
        vector_los_mayores.append(nuevo_nombre)
    elif nueva_edad > edad_mayor:
        edad_mayor = nueva_edad
        vector_los_mayores.clear()
        vector_los_mayores.append(nuevo_nombre)

# Comprobación inicial
nuevo_nombre = input("Introduzca nombre alumno: ")
if nuevo_nombre != "*":
    introducir_nueva_edad()

# Bucle hasta *
while nuevo_nombre != "*":
    nuevo_nombre = input("Introduzca nombre alumno: ")
    if nuevo_nombre != "*":
        introducir_nueva_edad()
   
# Resultados
print(f"Los alumnos mayores de edad son: {vector_mayores_edad}")
print(f"Los alumnos mayores tienen {edad_mayor} años y son: {vector_los_mayores}")