def calcular_fatorial(limite_multiplicacao):
    produto_fatorial = 1
    for multiplicador in range(1, limite_multiplicacao + 1):
        produto_fatorial *= multiplicador
    return produto_fatorial


def calcular_divisao(numerador_fracao, denominador_fracao):
    return numerador_fracao / denominador_fracao