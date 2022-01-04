if __name__ == '__main__':

    l = input().split()
    classic, notcool = int(l[0]), int(l[1])

    m = []

    for index in range(classic):
        m.append([int(col_i) for col_i in input().split()])

    t = t2 = 0
    found = False

    for i in range(1, classic-1):
        if found:
            break

        for j in range(1, notcool-1):
            if m[i][j] == 42:
                if m[i-1][j-1] == 7 and m[i-1][j] == 7 and m[i-1][j+1] == 7:
                    if m[i][j-1] == 7 and m[i][j + 1] == 7:
                        if m[i+1][j-1] == 7 and m[i+1][j] == 7 and m[i+1][j+1] == 7:
                            t = i+1
                            t2 = j+1
                            found = True
                            break

    print("{} {}".format(t, t2))
