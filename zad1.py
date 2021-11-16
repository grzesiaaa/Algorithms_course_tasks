def binomial_coeff(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return binomial_coeff(n-1, k-1) + binomial_coeff(n-1, k)


def exp_by_squaring(x, m):
    if m == 0:
        return 1
    elif m == 1:
        return x
    elif m % 2 == 0:
        return exp_by_squaring(x * x, m // 2)
    else:
        return x * exp_by_squaring(x * x, (m-1)//2)


def probability(n, k, p):
    prob = 0
    count_mult = "2k + log(n) + 3"
    power = exp_by_squaring(1-p, n)
    constant = p/(1-p)
    for i in range(0, k+1):
        prob += binomial_coeff(n, i) * power
        power *= constant
    return (prob, count_mult)




