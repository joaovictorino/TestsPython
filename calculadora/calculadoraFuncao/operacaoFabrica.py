from soma import executar as somar
from subtracao import executar as subtrair
from divisao import executar as dividir
from multiplicacao import executar as multiplicar
from operacaoDesabilitada import executar as desabilitada

def criar(operador, operadores):
    if operador in operadores:
        if operador == "+":
            return somar
        elif operador == "-":
            return subtrair
        elif operador == "/":
            return dividir
        elif operador == "*":
            return multiplicar
    else:
        return desabilitada
        