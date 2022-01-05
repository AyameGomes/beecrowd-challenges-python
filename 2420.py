if __name__ == '__main__':

    n = int(input())
    list1 = list(map(int, input().split()))

    sum1 = sum(list1)
    sum2 = 0
    i = 0

    for index in range(1, len(list1)):
        if(sum1 != sum2):

            sum2 += list1[(index * -1)]
            sum1 -= list1[(index * -1)]

        else:
            i = len(list1) - index + 1
            break

    print(i)
