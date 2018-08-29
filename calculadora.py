from operacao.operacaoFabrica import OperacaoFabrica

class Calculadora:

    def __init__(self, operadores):
        self.operacao = OperacaoFabrica(operadores)

    def calcular(self, valor1, valor2, operador):
        operacaoVal = self.operacao.criar(operador)
        return operacaoVal.executar(valor1, valor2)