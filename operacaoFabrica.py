from soma import Soma
from subtracao import Subtracao
from divisao import Divisao
from multiplicacao import Multiplicacao

class OperacaoFabrica:

    def criar(self, operador):
        if operador == "+":
            return Soma()
        elif operador == "-":
            return Subtracao()
        elif operador == "/":
            return Divisao()
        elif operador == "*":
            return Multiplicacao()