import timeit
from os import system

# Ejemplo de medición del tiempo de ejecución para una función
def resolver_ejercicio1(input_size):
    # El bucle "for" se ejecuta N veces
    for i in range(input_size):
        if i % 2 == 0:
            print(i)

def resolver_ejercicio2(input_size):
    # El bucle "for" se ejecuta N veces
    for i in range(input_size):
        if i % 2 == 0:
            print(i)
    for i in range(input_size):
        if i % 2 != 0:
            print (i)

def resolver_ejercicio3While(input_size):
    i = 1
    while (i < input_size):
        print (i)
        i = i * 2

def resolver_ejercicio3ForFor(input_size):
    for i in range(input_size):
        for j in range(i, input_size):
            print(f"{i},{j}")

def resolver_ejercicio4(input_size_A, input_size_B):
    for i in input_size_A.lenght():
        for j in (i, input_size_B.lenght()):
            print (input_size_A[i] + ',' + input_size_B[j]) 

def resolver_ejercicio5(input_size):
    for i in range(input_size):
        j = 1
        while j < input_size:
            print (j)
            j = j * 2
        
def resolver_ejercicio6(input_size):
    if input_size % 2 == 0:
        print ('par')
    else:
        print('inpar')

# Medición del tiempo para una entrada específica
input_size = 1000
execution_time = timeit.timeit(lambda: resolver_ejercicio3ForFor(input_size), number=1)
system('cls')
print(f"Tiempo de ejecución para input_size={input_size}: {execution_time} segundos")
