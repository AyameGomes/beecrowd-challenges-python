if __name__ == '__main__':

    while True:
        try:
            n = int(input())
            if n == 0:
                break

            presents = list(map(int, input().split()))
            presents.sort()

            presents_result = []

            for i in range(int(len(presents) / 2)):
                new_item = presents[i] + presents[((i + 1) * -1)]
                presents_result.append(new_item)

            print(f'{max(presents_result)} {min(presents_result)}')
        except EOFError:
            break
