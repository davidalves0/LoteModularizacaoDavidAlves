class OrdemCrescente:
    @staticmethod
    def calcularOrdem():
        valoresDiferentes = False
        
        while not valoresDiferentes:
            valor1 = int(input("Digite o primeiro valor: "))
            valor2 = int(input("Digite o segundo valor: "))
            
            if valor1 > valor2:
                valoresDiferentes = True
                menorValor = valor2
                maiorValor = valor1
            elif valor1 < valor2: 
                valoresDiferentes = True
                menorValor = valor1
                maiorValor = valor2
            else:
                valoresDiferentes = False
                print("Os valores devem ser diferentes. Tente novamente.\n")
                continue
        for contador in range(menorValor, maiorValor + 1):
            print(contador)