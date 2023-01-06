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
    return False, None, None, None, operations

def pythagorean_triple_2(length):
    operations = 0
    for a in range(1, length):
        for b in range(a, length):
            operations += 7
            c = length - a - b
            if a ** 2 + b ** 2 == c ** 2:
                return True, a, b, c, operations
    return False, None, None, None, operations

def pythagorean_triple_3(length):
    operations = 0
    for a in range(1, length//2):
        for b in range(a, length//2):
            operations += 7
            c = length - a - b
            if a ** 2 + b ** 2 == c ** 2:
                return True, a, b, c, operations
    return False, None, None, None, operations

def pythagorean_triple_4(length):
    operations = 0
    for a in range(1, length//3):
        operations += 14
        b = (2*a*length-length*length)//(2*(a-length))
        c = length - a - b
        if a * a + b * b == c * c:
            return True, a, b, c, operations
    return False, None, None, None, operations

def pythagorean_triple_5(length):
    c = 0
    m = 2
    operations = 0
    while c < length//2:
        for n in range(1, m):
            operations += 13
            a = m * m - n * n
            b = 2 * m * n
            c = m * m + n * n
            primitive_length = a + b + c
            if length % primitive_length == 0:
                operations += 5
                k = length // primitive_length
                a *= k
                b *= k
                c *= k
                return True, a, b, c, operations
        m += 1
    return False, None, None, None, operations
