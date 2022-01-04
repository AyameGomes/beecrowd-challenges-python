if __name__ == '__main__':

    languages = int(input())
    translations = {}

    for i in range(languages):
        original = str(input())
        translated = str(input())

        translations[original] = translated

    kids = int(input())

    for j in range(kids):
        kid_name = str(input())
        language = str(input())

        print(kid_name)
        print(translations[language])
        print('')
