class VelocidadeMedia:
    @staticmethod
    def calcularVelocidadeMedia(voltas: int, metros: int, tempominutos: int) -> float:
        percorrido = (int(voltas * metros))
        calculoKm = percorrido / 1000
        velocidadeMedia = calculoKm / (tempominutos / 60)
        return velocidadeMedia
