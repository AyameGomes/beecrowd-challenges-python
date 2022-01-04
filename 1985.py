if __name__ == '__main__':

    prices = {
        1001: 1.50,
        1002: 2.50,
        1003: 3.50,
        1004: 4.50,
        1005: 5.50
    }

    itens = int(input())
    total = 0

    for i in range(itens):
        item = list(map(int, input().split()))
        value = float(prices[item[0]]) * item[1]
        total += value

    print(f'{total:.2f}')
