from operacao.operacao import Operacao

@Operacao.register
class Divisao():

    def executar(self, valor1, valor2):
        return valor1 / valor2