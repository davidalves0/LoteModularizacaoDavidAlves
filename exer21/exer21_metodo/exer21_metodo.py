class MediaAluno:
    @staticmethod
    def calcularMedia():
        somatorioNotas = 0.0
        for semestre in range(1, 5, 1):
            notaAluno = int(input(f"Digite a nota do aluno referente ao {semestre}º semestre: "))
            somatorioNotas = somatorioNotas + notaAluno
        mediaAluno = somatorioNotas / 4
        print("A média do aluno é de", mediaAluno)
        if mediaAluno >= 6:
            print("APROVADO!")
        elif mediaAluno >= 3 and mediaAluno < 6:
            print("EXAME!")
        elif mediaAluno < 3:
            print("RETIDO!")