class NumeroMaior:
    @staticmethod
    def calcularMaior():
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f"O maior número entre {n1} e {n2} é: {maior}")
        