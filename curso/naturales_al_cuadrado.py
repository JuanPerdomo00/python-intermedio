#!/usr/bin/env python

def main():
    # lista = []
    #for i in range(1, 101):
        #if i % 3 != 0:
            #lista.append(i ** 2)

    

    lista = [i ** 2 for i in range(1, 101) if i % 3 != 0]
    print(lista)


if __name__ == '__main__':
    main()