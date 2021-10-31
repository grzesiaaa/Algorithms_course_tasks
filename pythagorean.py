import time
import math


def pythagorean_triple_1(l):
    operations = 0
    for a in range(1, l):
        for b in range(1, l):
            for c in range(1, l):
                operations += 9
                if a ** 2 + b ** 2 == c ** 2 and a + b + c == l:
                    return True, a, b, c, operations
    else:
        return False, None, None, None, operations

def pythagorean_triple_2(l):
    operations = 0
    for a in range(1, l):
        for b in range(a, l):
            operations += 7
            c = l - a - b
            if a ** 2 + b ** 2 == c ** 2:
                return True, a, b, c, operations
    else:
        return False, None, None, None, operations

def pythagorean_triple_3(l):
    operations = 0
    for a in range(1, l//2):
        for b in range(a, l//2):
            operations += 7
            c = l - a - b
            if a ** 2 + b ** 2 == c ** 2:
                return True, a, b, c, operations
    else:
        return False, None, None, None, operations

def pythagorean_triple_4(l):
    operations = 0
    for a in range(1, l//3):
        operations += 14
        b = (2*a*l-l*l)//(2*(a-l))
        c = l - a - b
        if a * a + b * b == c * c:
            return True, a, b, c, operations
    else:
        return False, None, None, None, operations


start = time.time()
for i in range(1,5000):
    pythagorean_triple_1(10)
print((time.time()-start)/5000)

start = time.time()
for i in range(1,5000):
    pythagorean_triple_2(10)
print((time.time()-start)/5000)

start = time.time()
for i in range(1,5000):
    pythagorean_triple_3(10)
print((time.time()-start)/5000)

start = time.time()
for i in range(1,5000):
    pythagorean_triple_4(10)
print((time.time()-start)/5000)



