from operacao.soma import Soma
from operacao.subtracao import Subtracao
from operacao.divisao import Divisao
from operacao.multiplicacao import Multiplicacao

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