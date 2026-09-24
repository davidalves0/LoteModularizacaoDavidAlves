class NovoPreco:
    @staticmethod
    def calcularNovoPreco(precoatual: float, mediadevendasmensal: int) -> float:
        if mediadevendasmensal < 500 and precoatual < 30:
            novoPreco = precoatual + (precoatual * 0.10)
        elif mediadevendasmensal >= 500 and mediadevendasmensal < 1000 and precoatual < 80:
            novoPreco = precoatual + (precoatual * 0.15)
        elif mediadevendasmensal >= 1000 and precoatual >= 80:
            novoPreco = precoatual - (precoatual * 0.05)
        else:
            novoPreco = precoatual
        return novoPreco