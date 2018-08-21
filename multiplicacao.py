from operacao import Operacao

@Operacao.register
class Multiplicacao():

    def executar(self, valor1, valor2):
        return valor1 * valor2