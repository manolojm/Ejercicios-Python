# 3_Listas

vector_notas = []
nota_media = 0

print("Introduzca 5 notas (0-10):")
for i in range(5):
    nueva_nota = int(input())
    vector_notas.append(nueva_nota)
    nota_media += nueva_nota
    
print(f"\nLista de notas: {vector_notas}")
print(f"La nota media es: {nota_media/5}")
print(f"La nota más alta es: {max(vector_notas)}")
print(f"La nota ás baja es: {min(vector_notas)}")