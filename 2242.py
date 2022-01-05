if __name__ == '__main__':

    n = input()

    def removeCons(s):
        vowel = "aeiouAEIOU"

        lis = [i for i in s]
        for i in range(len(s)):
            k = 0
            for j in range(len(vowel)):
                if(s[i] != vowel[j]):
                    k += 1
            if(k == 10):
                lis[i] = 0
        s = "".join(i for i in lis if(i != 0))
        return(s)

    word = removeCons(n)

    if (word == word[::-1]):
        print('S')
    else:
        print('N')
