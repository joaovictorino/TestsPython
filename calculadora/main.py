#!/bin/python3

import math
import os
import random
import re
import sys
from calculadora import Calculadora


if __name__ == '__main__':
    print("Informe as operações habilitadas (+) soma (-) subtração (*) multiplicação (/) divisão:")
    operadores = input()
    continuar = "S"
    teste = Calculadora(operadores)
    while continuar == "S":
        print("Informe valor 1:")
        a = int(input())
        print("Informe valor 2:")
        b = int(input())
        print("Informe a operação:")
        c = input()
        d = teste.calcular(a, b, c)
        print("Resultado: " + str(d))
        print("Desejar continuar? S/N")
        continuar = input()