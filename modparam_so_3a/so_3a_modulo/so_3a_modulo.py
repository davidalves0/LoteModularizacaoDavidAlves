class LoFatorial:
    @staticmethod
    def calcularfatorialdasilva(valor: int) -> int:
        for contador in range (1, valor, 1):
            valor = valor * contador
        return valor
