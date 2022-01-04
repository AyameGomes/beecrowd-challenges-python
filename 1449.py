if __name__ == '__main__':

    runs = int(input())
    for times in range(runs):

        dict_songs = {}

        m, n = map(int, input().split())

        for i in range(m):
            japanese = str(input())
            portuguese = str(input())
            dict_songs[japanese] = portuguese

        for j in range(n):
            songs = list(map(str, input().split()))
            resultado = ''

            for word in songs:
                if word in dict_songs:
                    resultado += (dict_songs[word] + ' ')
                else:
                    resultado += (word + ' ')
            print(resultado.strip())

        print('')
