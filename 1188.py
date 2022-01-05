if __name__ == '__main__':

    op = input()

    matrix = []

    for i in range(12):
        line = []

        for j in range(12):
            value = float(input())
            line.append(value)

        matrix.append(line)

    result = 0
    inferior = 5
    superior = 7
    itens = 0

    for i in range(7, 12):
        for j in range(inferior, superior):
            result += matrix[i][j]
            itens += 1
        inferior -= 1
        superior += 1

    if op == 'M':
        result = result / itens

    print(f'{result:.1f}')
