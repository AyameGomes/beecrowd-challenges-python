if __name__ == '__main__':

    n = str(input())

    one = 0
    for index in range(len(n)):
        if (n[index] == '1'):
            one += 1

    if (one % 2 == 0):
        n += '0'

    else:
        n += '1'

    print(n)
