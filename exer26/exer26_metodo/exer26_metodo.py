class MultiploDoMenor:
    def calcularMultiplo():
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        if num2 > num1:
            maior = num2
            menor = num1
        else: 
            maior = num1
            menor = num2
        if maior % menor == 0:
            print("Múltiplo")
        else:
            print("Não é múltiplo")