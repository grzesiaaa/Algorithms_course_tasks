import time
import math


def pythagorean_triple_1(length):
    operations = 0
    for a in range(1, length):
        for b in range(1, length):
            for c in range(1, length):
                operations += 9
                if a ** 2 + b ** 2 == c ** 2 and a + b + c == length:
                    return True, a, b, c, operations
    else:
        return False, None, None, None, operations

def pythagorean_triple_2(length):
    operations = 0
    for a in range(1, length):
        for b in range(a, length):
            operations += 7
            c = length - a - b
            if a ** 2 + b ** 2 == c ** 2:
                return True, a, b, c, operations
    else:
        return False, None, None, None, operations

def pythagorean_triple_3(length):
    operations = 0
    for a in range(1, length//2):
        for b in range(a, length//2):
            operations += 7
            c = length - a - b
            if a ** 2 + b ** 2 == c ** 2:
                return True, a, b, c, operations
    else:
        return False, None, None, None, operations

def pythagorean_triple_4(length):
    operations = 0
    for a in range(1, length//3):
        operations += 14
        b = (2*a*length-length*length)//(2*(a-length))
        c = length - a - b
        if a * a + b * b == c * c:
            return True, a, b, c, operations
    else:
        return False, None, None, None, operations
