if __name__ == '__main__':

    morse_code = {'=.===': 'a', '===.=.=.=': 'b',  '===.=.===.=': 'c',  '===.=.=': 'd', '=': 'e',  '=.=.===.=': 'f', '===.===.=': 'g',  '=.=.=.=': 'h', '=.=': 'i', '=.===.===.===': 'j', '===.=.===': 'k', '=.===.=.=': 'l',  '===.===': 'm',
                  '===.=': 'n', '===.===.===': 'o', '=.===.===.=': 'p', '===.===.=.===': 'q', '=.===.=': 'r', '=.=.=': 's', '===': 't', '=.=.===': 'u',  '=.=.=.===': 'v',  '=.===.===': 'w',  '===.=.=.===': 'x', '===.=.===.===': 'y', '===.===.=.=': 'z'}

    cases = int(input())

    for k in range(cases):
        case = input()
        case = case.split('.......')

        for word in range(len(case)):

            individual_case = case[word]
            individual_case = individual_case.split('...')

            for i in range(len(individual_case)):

                print(morse_code[individual_case[i]], end='')

            if word != len(case) - 1:

                print(end=' ')

        print()
