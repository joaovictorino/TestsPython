from operacao import Operacao

@Operacao.register
class Soma():

    def executar(self, valor1, valor2):
        return valor1 + valor2