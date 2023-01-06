def ordinary_polynomial_value_calc(coeff, arg):
    result = 0
    count_mult = 0
    j = len(coeff)
    count_add = j - 1
    for i in reversed(coeff):
        result += i * arg**(j-1)
        count_mult += j - 1
        j -= 1
    return result, count_mult, count_add


def smart_polynomial_value_calc(coeff, arg):
    result = 0
    count_mult = len(coeff) - 1
    count_add = len(coeff) - 1
    for i in reversed(coeff):
        result = result * arg + i
    return result, count_mult, count_add

