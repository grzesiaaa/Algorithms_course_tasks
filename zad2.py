def horner(coefficients, x):
    if type(coefficients) == list:
        result = 0
        multiplies = 0
        for i in reversed(coefficients):
            result = result * x + i
            multiplies +=1
        return result, multiplies - 1
    else:
        raise TypeError("Coefficients must be a list.")


print(horner([11, 0, 3, 3, 8], 4))
