if __name__ == '__main__':

    while True:
        number = int(input())

        if number == 0:
            break

        list = []

        for i in range(number):
            list.append([])
            for j in range(number):
                list[i].append(0)

        list[0][0] = 1
        for i in range(0, number):
            if i >= 1:
                list[i][0] = list[i - 1][0] * 2

            for j in range(1, number):
                list[i][j] = list[i][j-1] * 2

        T = len(str(list[number-1][number-1]))
        for i in range(number):
            for j in range(number):
                list[i][j] = str(list[i][j])
                while len(list[i][j]) < T:
                    list[i][j] = ' ' + list[i][j]
            M = ' '.join(list[i])

            print(M)
        print()
