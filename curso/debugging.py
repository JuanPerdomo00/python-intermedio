#!/usr/bin/env python3

def divisor(n):
    divisoir = [i for i in range(1, n + 1) if n % i == 0]
    #breakpoint()
    return divisoir

def main():
    n = int(input('Ingresa un numero: '))
    print(divisor(n))
    print('termino mi programa')

if __name__ == '__main__':
    main()