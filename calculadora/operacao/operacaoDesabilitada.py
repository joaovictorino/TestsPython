from operacao.operacao import Operacao

@Operacao.register
class OperacaoDesabilitada():

    def executar(self, valor1, valor2):
        return "Operação desabilitada."