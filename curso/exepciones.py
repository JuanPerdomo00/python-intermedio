#!/usr/bin/env python3

def divisor(n: int) -> int:
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors




def main():
    try:
        n = int(input('Ingrese un numero: '))
        if n < 0:
            raise ValueError('Tiene que ser un positivo')
        print(divisor(n))
        print('\ntermino el programa')
    except ValueError as ve:
        print(ve)

    
if __name__ == '__main__':
    main()