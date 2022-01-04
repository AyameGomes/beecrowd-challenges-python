if __name__ == '__main__':

    array = []

    tests = int(input())
    for a in range(tests):

        falso = False
        matrix = []

        for i in range(9):
            matrix.append(list(map(int, input().split(" "))))

        for linha in matrix:
            for coluna in linha:
                if linha.count(coluna) > 1:
                    falso = True

        for i in range(9):
            x = []
            for linha in matrix:
                if not(linha[i] in x):
                    x.append(linha[i])
            if len(x) != 9:
                falso = True

        for linham in range(0, 9, 3):
            x1 = []
            x2 = []
            x3 = []
