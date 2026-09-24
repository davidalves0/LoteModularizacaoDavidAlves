from exer29_modulo.exer29_modulo import TipoInvestimento

if __name__ == "__main__":
    tipoinvestimento = int(input("Digite o tipo de investimento (1 ou 2): "))
    valorinvestimento = float(input("Digite o valor do investimento: "))
    if tipoinvestimento == 1:
        print("Você escolheu o tipo POUPANÇA")
    elif tipoinvestimento == 2:
        print("Você escolheu o tipo RENDA FIXA")
    novovalor = TipoInvestimento.calcularNovoInvestimento(tipoinvestimento, valorinvestimento)
    print(f"Após o período de 30 dias, seu valor investido se transformou em: R$ {novovalor:.2f}")