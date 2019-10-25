from operacao.soma import Soma
from operacao.subtracao import Subtracao
from operacao.divisao import Divisao
from operacao.multiplicacao import Multiplicacao
from operacao.operacaoDesabilitada import OperacaoDesabilitada

class OperacaoFabrica:

    def __init__(self, operadores):
        self.operadores = operadores

    def criar(self, operador):
        if operador in self.operadores:
            if operador == "+":
                return Soma()
            elif operador == "-":
                return Subtracao()
            elif operador == "/":
                return Divisao()
            elif operador == "*":
                return Multiplicacao()
        else:
            return OperacaoDesabilitada()