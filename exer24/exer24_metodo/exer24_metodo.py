class DivisivelPor:
    def divisivelPor2e3():
        numero = int(input("Digite um número inteiro: "))
        if numero % 2 == 0 and numero % 3 == 0:
            print("Divisível por 2 e 3")
        else:
            print("Não é divisível por 2 e 3")