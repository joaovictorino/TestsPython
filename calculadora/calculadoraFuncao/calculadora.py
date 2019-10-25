from operacaoFabrica import criar

def calcular(valor1, valor2, operador, operadores):
    executar = criar(operador, operadores)
    return executar(valor1, valor2)