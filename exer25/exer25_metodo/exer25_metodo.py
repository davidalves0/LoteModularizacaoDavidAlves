class HoraJogo:
    def calcularHoraJogo():
        hora_inicio = int(input("Digite a hora de início: "))
        minuto_inicio = int(input("Digite o minuto de início: "))
        hora_fim = int(input("Digite a hora de término: "))
        minuto_fim = int(input("Digite o minuto de término: "))
        if minuto_fim < minuto_inicio:
            minuto_fim = minuto_fim + 60
            hora_fim = hora_fim - 1
        if hora_fim < hora_inicio:
            hora_fim = hora_fim + 24
        duracao_horas = hora_fim - hora_inicio
        duracao_minutos = minuto_fim - minuto_inicio
        print("Duração do jogo: {} horas e {} minutos".format(duracao_horas, duracao_minutos))