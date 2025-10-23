# 23_Fibonacci

numero = int(input("Introduzca el numero para calcular su fibonacci: "))
anterior_1 = 0;
anterior_2 = 1;

if numero == 0:
    print(anterior_1)
elif numero == 1:
    print(anterior_2)
else:
    for i in range(2, numero+1):
        anterior_tmp = anterior_2;
        anterior_2 = anterior_1 + anterior_2;
        anterior_1 = anterior_tmp;
        print(anterior_2)