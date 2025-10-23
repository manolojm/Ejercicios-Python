# 4_Volumen_de_un_cono

radio = float(input("Introduzca el radio del cono: "))
altura = float(input("Introduzca la altura del cono: "))

volumen = round((1/3) * 3.14 * (radio*radio) * altura, 2);

print(f"El volumen de su cono son: {volumen} centimetro cuadrados")