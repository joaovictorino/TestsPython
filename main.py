#!/bin/python3

import math
import os
import random
import re
import sys
from calculadora import Calculadora


if __name__ == '__main__':
    print("Informe valor 1:")
    a = int(input())
    print("Informe valor 2:")
    b = int(input())
    print("Informe a operação:")
    c = input()
    teste = Calculadora()
    d = teste.calcular(a, b, c)
    print("Resultado: " + str(d))