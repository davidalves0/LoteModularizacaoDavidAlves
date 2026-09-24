class DifMaiorMenor:

    @staticmethod
    def Diferenca():
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))
        if n1 > n2:
            dif = n1 - n2
        else:
            dif = n2 - n1
        print(f"A diferença entre {n1} e {n2} é: {dif}")
