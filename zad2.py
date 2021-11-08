import time


def ordinary_polynomial_value_calc(coeff, arg):
    if type(coeff) == list:
        result = 0
        count_mult = 0
        count_add = 0
        j = len(coeff)
        for i in reversed(coeff):
            result += i * arg**(j-1)
            count_add += 1
            count_mult += j
            j -= 1
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


start_1 = time.time()
for _ in range(10000):
    smart_polynomial_value_calc([11, -2, 3, 3], 4)
print(smart_polynomial_value_calc([11, -2, 3, 3], 4))
print(time.time() - start_1)
start_2 = time.time()
for _ in range(10000):
    ordinary_polynomial_value_calc([11, -2, 3, 3], 4)
print(ordinary_polynomial_value_calc([11, -2, 3, 3], 4))
print(time.time() - start_2)
