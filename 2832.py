
if __name__ == '__main__':

    numHatches, numChickens = map(int, input().split())
    listHat = list(map(int, input().split()))

    start = 1
    end = 10 ** 8

    while (start < end):
        day = (start + end) // 2

        sumChickens = 0

        for index in range(len(listHat)):
            sumChickens += day // listHat[index]

        if (sumChickens < numChickens):
            start = day + 1
        else:
            end = day

    print(start)
