if __name__ == '__main__':

    tests = int(input())
    for test in range(tests):
        n = int(input())
        itens = []

        for i in range(n):
            new_itens = list(map(str, input().split()))
            itens.append(new_itens)

        itens = dict(itens)

        total = 0
        o = int(input())
        for i in range(o):
            new_buy = list(map(str, input().split()))
            what_bought = float(itens[new_buy[0]])
            spent = what_bought * int(new_buy[1])
            total += spent

        print(f'R$ {total:.2f}')
