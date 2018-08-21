from operacao.operacaoFabrica import OperacaoFabrica

class Calculadora:

    def calcular(self, valor1, valor2, operador):
        operacao = OperacaoFabrica()
        operacaoVal = operacao.criar(operador)
        return operacaoVal.executar(valor1, valor2)