# Questão 8 - notas.

def calcular_nota(respostas_aluno):
    gabarito = ['A', 'B', 'C', 'D', 'E', 'E', 'D', 'C', 'B', 'A']
    acertos = sum(1 for i in range(10) if respostas_aluno[i] == gabarito[i])
    return acertos

def main():
    notas = []

    while True:
        respostas_aluno = []
        print("responda as questões: (A, B, C, D, E)")

        for i in range(1, 11):
            resposta = input(f"questão {i}: ").upper()
            respostas_aluno.append(resposta)

        acertos = calcular_nota(respostas_aluno)
        notas.append(acertos)
        print(f"nota: {acertos} pontos.")

    if notas:
        maior_acerto = max(notas)
        menor_acerto = min(notas)
        total_alunos = len(notas)
        media_notas = sum(notas) / total_alunos

        print(f"\nmaior Acerto: {maior_acerto}")
        print(f"menor Acerto: {menor_acerto}")
        print(f"total de Alunos: {total_alunos}")
        print(f"maédia das Notas: {media_notas:.2f}")

if __name__ == "__main__":
    main()