if __name__ == '__main__':

    n = int(input())
    op = input()

    matrix = []

    for i in range(12):
        line = []

        for j in range(12):
            value = float(input())
            line.append(value)

        matrix.append(line)

    if op == 'S':
        result = sum(matrix[n])

    if op == 'M':
        result = (sum(matrix[n]) / 12)

    print(f'{result:.1f}')
