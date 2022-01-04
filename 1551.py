if __name__ == '__main__':

    n = int(input())

    for i in range(n):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        phrase = str(input())

        phrase = phrase.lower()

        contains = 0

        for i in range(len(alphabet)):
            if alphabet[i] in phrase:
                contains += 1

        if contains == 26:
            print('frase completa')

        elif contains >= 13:
            print('frase quase completa')

        elif contains < 13:
            print('frase mal elaborada')
