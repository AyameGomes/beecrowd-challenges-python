if __name__ == '__main__':

    while True:
        alunos = {}

        n = int(input())

        if n == 0:
            break

        for i in range(n):
            novo_aluno = list(map(str, input().split()))
            alunos[novo_aluno[0]] = novo_aluno[1]

        m = int(input())
        falsas = 0
        erro = 0
        for j in range(m):
            contador = 0
            aluno_presente = list(map(str, input().split()))

            for y in alunos[aluno_presente[0]]:
                if y != aluno_presente[1][contador]:
                    erro += 1
                contador += 1

            if erro >= 2:
                falsas += 1

            erro = 0

        print(falsas)
