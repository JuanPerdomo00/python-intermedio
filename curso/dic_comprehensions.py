#!/usr/bin/env python3

from math import sqrt

def challenge():
    '''Crea, cun un dictionary comprehension, un 
    diccionario cuyas llaves sean los 1000 primero numeros
    naturales con sus raices cuadradas cono valores
    '''

    challenge = {i: sqrt(i) for i in range(1, 1001)}
    print(challenge)


def main():
    challenge()
    diccionario = {}

    for i in range(1, 101):
        if i % 3 != 0:
            diccionario[i] = i**3
    
    #print(diccionario)


    #for key, value in diccionario.items():
    #   print(f'{key} elevado al cuadrado  es : {value}')
    #    break

    diccionario = {i: i**3 for i in range(1,101) if i % 3 != 0}
    # print(diccionario)



if __name__ == '__main__':
    main()
