from exer27_modulo.exer27_modulo import VelocidadeMedia

if __name__ == "__main__":
    voltas = int(input("Digite o número de voltas: "))
    metros = int(input("Digite o total em metros do circuito: "))
    tempominutos = int(input("Digite o tempo em minutos: "))
    velocidadeMedia = VelocidadeMedia.calcularVelocidadeMedia(voltas, metros, tempominutos)
    print(f"A velocidade média do carro foi de: {velocidadeMedia:.2f} km/h")