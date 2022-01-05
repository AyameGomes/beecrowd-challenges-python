if __name__ == '__input__':

    n = int(input())
    for program in range(n):
        caso = program + 1
        total, usadas = map(int, input().split())
        renas = []

        for i in range(total):
            nova_rena = list(map(str, input().split()))
            renas.append(nova_rena)

            for i in range(len(renas)):
                for j in range(1, 3):
                    renas[i][j] = float(renas[i][j])

            renas = sorted(renas, key=lambda x: (-x[1], x[2], x[3], x[0]))

            print(f'CENARIO {({caso})}')
            for whatever in range(usadas):
                posicao = whatever + 1
                rena_atual = renas[whatever][0]
                print(f'{posicao} - {rena_atual}')
