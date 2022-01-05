if __name__ == '__main__':

    n = int(input())

    for i in range(n):
        a, b = map(str, input().split())
        c = ''

        if len(a) > len(b):
            for i in range(len(b)):
                c += a[i]
                c += b[i]
            c += a[len(b):]

        elif (len(b)) > len(a):
            for i in range(len(a)):
                c += a[i]
                c += b[i]
            c += b[len(a)::]

        elif (len(a) == len(b)):
            for i in range(len(a)):
                c += a[i]
                c += b[i]

        print(c)
