 while True:
      number = int(input())

       if number == 0:
            break

        whatever = []

        for i in range(number):
            whatever.append([])
            for j in range(number):
                whatever[i].append(0)

        whatever[0][0] = 1
        for i in range(0, number):
            if i >= 1:
                whatever[i][0] = whatever[i - 1][0] * 2

            for j in range(1, number):
                whatever[i][j] = whatever[i][j-1] * 2

        T = len(str(whatever[number-1][number-1]))
        for i in range(number):
            for j in range(number):
                whatever[i][j] = str(whatever[i][j])
                while len(whatever[i][j]) < T:
                    whatever[i][j] = ' ' + whatever[i][j]
            M = ' '.join(whatever[i])

            print(M)
        print()
