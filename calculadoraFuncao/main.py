#!/bin/python3

import math
import os
import random
import re
import sys
from calculadora import calcular


if __name__ == '__main__':
    print("Informe as operações válidas (+) soma (-) subtração (*) multiplicação (/) divisão:")
    operadores = input()
    continuar = "S"
    while continuar == "S":
        print("Informe valor 1:")
        a = int(input())
        print("Informe valor 2:")
        b = int(input())
        print("Informe a operação:")
        c = input()
        d = calcular(a, b, c, operadores)
        print("Resultado: " + str(d))
        print("Desejar continuar? S/N")
        continuar = input()