from modparam_so_3b_modulo.modparam_so_3b_modulo import calcular_fatorial, calcular_divisao

if __name__ == "__main__":
    limite_termos_serie = int(input("Digite um valor inteiro e positivo para N: "))
    soma_acumulada_serie = 1.0

    for termo_atual in range(1, limite_termos_serie + 1):
        fatorial_termo_atual = calcular_fatorial(termo_atual)
        valor_fracao_atual = calcular_divisao(1, fatorial_termo_atual)
        soma_acumulada_serie += valor_fracao_atual

    print(f"\nO resultado da série para N = {limite_termos_serie} é: {soma_acumulada_serie:.6f}")