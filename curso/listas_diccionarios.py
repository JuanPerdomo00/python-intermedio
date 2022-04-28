#!/usr/bin/env python3

def main():
    my_list = [1,'hello', True, 1.4]
    my_dic = {'nombre': 'juan', 'apellido': 'perdomo'}

    super_list = [
        {'nombre': 'juan', 'apellido': 'perdomo'},
        {'nombre': 'pepe', 'apellido': 'pepero'},
        {'nombre': 'alone', 'apellido': 'alones'},
        {'nombre': 'gustav', 'apellido': 'argv'}
    ]

    super_dic = {
        "narutar num": [1,2,3,4,5],
        "integer nums": [-1,-2,0,1,2],
        "floating num": [1.1, 4.3, 3.4]
    }


    for key, value in super_dic.items():
         print(f'{key} - {value}')

    for lista in super_list:
        print(f'{lista}')

if __name__ == '__main__':
    main()