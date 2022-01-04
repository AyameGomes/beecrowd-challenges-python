if __name__ == '__main__':

    a = int(input())

    for case in range(a):
        case = int(input())
        students = list(map(str, input().split()))
        classes = list(map(str, input().split()))

        not_passed = []

        for i in range(len(students)):
            present = 0
            valid = 0

            for j in range(len(classes[i])):
                if classes[i][j] == 'P':
                    present += 1
                    valid += 1
                if classes[i][j] == 'A':
                    valid += 1

            if present < ((75 / 100) * valid):
                not_passed.append(students[i])

        print(*not_passed, sep=" ")
