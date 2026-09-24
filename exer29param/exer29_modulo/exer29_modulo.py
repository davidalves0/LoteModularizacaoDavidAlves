class TipoInvestimento:
    @staticmethod
    def calcularNovoInvestimento(tipoinvestimento: int, valorinvestimento: float) -> float:
        if tipoinvestimento == 1:
            novoValor = valorinvestimento + (valorinvestimento * 0.03)
        elif tipoinvestimento == 2:
            novoValor = valorinvestimento + (valorinvestimento * 0.05)
        return novoValor