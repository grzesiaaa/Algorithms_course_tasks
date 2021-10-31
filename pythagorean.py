import time

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
        for b in range(1, l):
            operations += 11
            c = l - a - b
            if a ** 2 + b ** 2 == c ** 2 and a + b + c == l:
                return True, a, b, c, operations
    else:
        return False, None, None, None, operations

def pythagorean_triple_3(l):
    operations = 0
    for a in range(1, l):
        for b in range(a, l):
            operations += 7
            c = l - a - b
            if a ** 2 + b ** 2 == c ** 2:
                return True, a, b, c, operations
    else:
        return False, None, None, None, operations

def pythagorean_triple_4(l):
    operations = 0
    for a in range(1, l//2):
        for b in range(a, l//2):
            operations += 7
            c = l - a - b
            if a ** 2 + b ** 2 == c ** 2:
                return True, a, b, c, operations
    else:
        return False, None, None, None, operations

def pythagorean_triple_5(l):
    operations = 0
    for a in range(1, l//3):
        operations += 14
        b = (2*a*l-l**2)//(2*(a-l))
        c = l - a - b
        if a ** 2 + b ** 2 == c ** 2:
            return True, a, b, c, operations
    else:
        return False, None, None, None, operations

"""start = time.time()
print(pythagorean_triple_4(1000))
print(time.time()-start)"""

start = time.time()
for i in range(1,1000):
    pythagorean_triple_5(1000)
print((time.time()-start)/1000)
print(pythagorean_triple_5(1000))
#jakas tabelka w raporcie ile operacji jedna druga trzecia metoda