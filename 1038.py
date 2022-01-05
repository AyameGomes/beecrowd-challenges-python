if __name__ == '__main__':

    i, n = map(int, input().split())

    itens = [4, 4.5, 5, 2, 1.5]

    def find_total(i, n):
        value = itens[i - 1]
        price = value * n
        return price

    print(f'Total: R$ {(find_total(i, n)):.2f}')
