if __name__ == '__main__':

    from math import gcd

    a, b, c, d = (map(int, input().split()))

    result_a = 0
    result_b = 0

    if (b == d):
        result_a = a + c
        result_b = b
    else:
        mult_1 = b * c
        mult_2 = d * a
        mult_3 = b * d

        result_a = mult_1 + mult_2
        result_b = mult_3

    d = gcd(result_a, result_b)

    result_a = result_a / d
    result_b = result_b / d

    print(f'{result_a:.0f} {result_b:.0f}')
