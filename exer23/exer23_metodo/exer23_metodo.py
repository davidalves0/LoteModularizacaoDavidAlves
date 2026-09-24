class OrdemCrescente02:
    @staticmethod
    def calcularOrdem():
        n1 = int(input("Digite o 1º valor: "))
        n2 = int(input("Digite o 2º valor (deve ser maior que o 1º): "))
        n3 = int(input("Digite o 3º valor (deve ser maior que o 2º): "))
        if n1 > n2 or n2 > n3:
            print("Algum dos 3 primeiros valores não está em ordem crescente!")
        else:
            n4 = int(input("Digite o 4º valor: "))
        if n4 >= n3:
            print(f"Ordem crescente: {n1}, {n2}, {n3}, {n4}")
        elif n4 >= n2:
            print(f"Ordem crescente: {n1}, {n2}, {n4}, {n3}")
        elif n4 >= n1:
            print(f"Ordem crescente: {n1}, {n4}, {n2}, {n3}")
        else:
            print(f"Ordem crescente: {n4}, {n1}, {n2}, {n3}")