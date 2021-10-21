import time

def pythagorean_triple_1(l):
    for a in range(1, l):
        for b in range(1, l):
            for c in range(1, l):
                if a ** 2 + b ** 2 == c ** 2 and a + b + c == l:
                    return a, b, c


def pythagorean_triple_2(l):
    for a in range(1, l):
        for b in range(1, l):
            c = l - a - b
            if a ** 2 + b ** 2 == c ** 2 and a + b + c == l:
                return a, b, c


def pythagorean_triple_3(l):
    for a in range(1, l):
        for b in range(a, l):
            c = l - a - b
            if a ** 2 + b ** 2 == c ** 2:
                return a, b, c


def pythagorean_triple_4(l):
    for a in range(1, l//2):
        for b in range(a, l//2):
            c = l - a - b
            if a ** 2 + b ** 2 == c ** 2:
                return a, b, c


def pythagorean_triple_5(l):
    for a in range(1, l//3):
        b = (2*a*l-l**2)//(2*(a-l))
        c = l - a - b
        if a ** 2 + b ** 2 == c ** 2:
            return a, b, c


print(pythagorean_triple_5(4392))
