def ordinary_polynomial_value_calc(coeff, arg):
    if type(coeff) == list:
        result = 0
        count_mult = 0
        count_add = 0
        j = len(coeff)
        for i in reversed(coeff):
            result += i * arg**(j-1)
            j -= 1
            count_add += 1
            count_mult += 1
        return result, count_mult, count_add - 1


def smart_polynomial_value_calc(coeff, arg):
    if type(coeff) == list:
        result = 0
        count_mult = 0
        count_add = 0
        for i in reversed(coeff):
            result = result * arg + i
            count_mult += 1
            count_add += 1
        return result, count_mult - 1, count_add - 1
    else:
        raise TypeError("Coefficients must be a list.")


print(smart_polynomial_value_calc([11, -2, 3, 3], 4))
print(ordinary_polynomial_value_calc([11, -2, 3, 3], 4))

list = [1,2,3]
print(list.index(1))
print(len(list))