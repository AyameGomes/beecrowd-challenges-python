if __name__ == '__main__':

    while True:
        try:
            cipher, classic = [int(letterx) for letterx in input().split()]
            hunf = []
            for index in range(cipher):
                hunf.append(input().split())

            lettera = [(index, j.index('2'))
                       for index, j in enumerate(hunf) if '2' in j]
            letterb = [(index, j.index('1'))
                       for index, j in enumerate(hunf) if '1' in j]

            letterx = (abs(lettera[0][0] - letterb[0][0]))
            lettery = (abs(lettera[0][1] - letterb[0][1]))
            print(letterx + lettery)

        except EOFError:
            break
