#!/usr/bin/env python3
# Copyright (c) 2022 Python Software Foundation (jakepy)
# High order functions: filter, map, reduce
# Es una funcion que resive como parametro a otra funcion 

# ejemplo de funcion nque recibe otra funcion 

def hola():
    print("Hola")

def adios():
    print("Adios")

def saludar(func):
    func()

# saludar(hola)
# saludar(adios)
'''
filter

tenemos una lista de numeros aleatorios [1,4,5,6,9,13,19,21]
y quiero tener una lista de estos numeros pero solamente los que 
son impares [1,5,9,13,19,21]
'''

# solucion con list comprehension
def solution_list_completion():
    list_num = [1,4,5,6,9,13,19,21]
    list_impar = [i for  i in list_num if i % 2 != 0]
    print(list_impar)

# solucion con filter
my_list = [1,4,5,6,9,13,19,21]
odd = list(filter(lambda x: x % 2 != 0, my_list))
# print(odd)


'''
map

tenemos una lista de los numeros del 1 al 5 [1,2,3,4,5], y lo que quiero
hacer es convertir a esta lista en la misma pero con los numeros elevados al
cuadrado.
'''

# solucion con list comprehension
lists = [1,2,3,4,5]
solution_list = [i **2 for i in lists]
# print(solution_list)

# solucion con map
my_list = [1,2,3,4,5]
odd = list(map(lambda x: x**2, my_list))
# print(odd)


'''
reduce

tenemos una lista con [2,2,2,2,2] como redusco los valores de esta lista
'''

# solucion sin reduce 
my_list = [2,2,2,2,2]

all_multiplied = 1

for i in my_list:
    all_multiplied *= i

# print(all_multiplied)


# solucion con reduce
from functools import reduce

my_list = [2,2,2,2,2]

all_multiplied = reduce(lambda a,b: a * b, my_list)

print(all_multiplied)