#!/usr/bin/env python3
# 
# Funciones lambdas o funciones anonimas
# lambda argumentos: exprecion
# las funciones lambdas pueden tener los argumentos que necesitemos
# pero sola mente una sola linea de codigo, una sola exprecion 

# asi seria con una funcion noermal
def es_palindromo(string):
    return string == string[::-1]

print(es_palindromo("ana"))

# asi es con una funcion anonima
palindromo = lambda string: string == string[::-1]

print(palindromo('ana'))