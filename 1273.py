if __name__ == '__main__':

    runs = 0
    while True:
        n = int(input())

        if n == 0:
            break

        a = []
        for i in range(n):
            a.append(input())

        b = 0
        for i in range(len(a)):
            if len(a[i]) > b:
                b = len(a[i])

        if runs != 0:
            print('')
        for palavra in a:
            if len(palavra) < b:
                nova_palavra = (' ' * (b - len(palavra))) + palavra
                print(nova_palavra)
            else:
                print(palavra)

        runs += 1
