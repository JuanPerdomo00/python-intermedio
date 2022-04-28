#!/usr/bin/env python3


def divisor(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors


def main():
    n = input('Ingrese un numero: ')
    assert n.isnumeric() and int(n) < 0, 'Ingresa solo numeros positivos'
    print(divisor(int(n)))
    print('Termino el programa')

if __name__ == '__main__':
    main()