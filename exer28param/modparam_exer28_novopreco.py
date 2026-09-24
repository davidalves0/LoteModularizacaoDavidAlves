from exer28_metodo.exer28_metodo import NovoPreco

if __name__ == "__main__":
    preco = float(input("Digite o valor atual do produto:"))
    mediamensal = int(input("Digite a média mensal de vendas do produto: "))
    novopreco = NovoPreco.calcularNovoPreco(preco, mediamensal)
    print(f"O novo preço do produto é: R$ {novopreco:.2f}")