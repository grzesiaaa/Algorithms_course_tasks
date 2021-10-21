def pythagorean_triple(l):
    for a in range(1,l):
        for b in range(1, l):
            for c in range(1, l):
                if a**2 + b**2 == c **2 and a+b+c==l:
                    print(a,b,c)


pythagorean_triple(1000)
