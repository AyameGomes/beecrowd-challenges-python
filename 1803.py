if __name__ == '__main__':

    a = str(input())
    b = str(input())
    c = str(input())
    d = str(input())

    f = int(a[0] + b[0] + c[0] + d[0])
    l = int(a[-1] + b[-1] + c[-1] + d[-1])

    result = ''

    for i in range(1, (len(a) - 1)):
        code = int(a[i] + b[i] + c[i] + d[i])
        code = (f * code + l) % 257
        code = chr(code)
        result += code

    print(result)
