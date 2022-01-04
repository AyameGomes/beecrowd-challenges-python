if __name__ == '__main__':

    last_week, last_two_days = map(int, input().split())

    num_two_days = list(map(int, input().split()))

    for i in range(last_week):
        ident = int(input())

        if ident in num_two_days:
            print('0')
        else:
            print('1')

        num_two_days.append(ident)
