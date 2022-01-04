if __name__ == '__main__':

    while True:
        try:
            notes = {
                'W': 1,
                'H': 1/2,
                'Q': 1/4,
                'E': 1/8,
                'S': 1/16,
                'T': 1/32,
                'X': 1/64
            }

            n = str(input())

            if n == '*':
                break
            n = n.replace('/', ' ')
            n = list(n.split())

            corrects = 0

            for word in n:
                duration = 0
                for i in word:
                    duration += notes[i]
                if duration == 1:
                    corrects += 1

            print(corrects)

        except EOFError:
            break
