if __name__ == '__main__':

    n = int(input())

    for i in range(n):
        strings = list(map(str, input().split()))

        strings = sorted(strings, reverse=True, key=len)

        print(" ".join(str(x) for x in strings))
