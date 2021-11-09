"""def check(n, k, p):
    if n < 0 or k < 0:
        raise ValueError("n and k should be greater than 0.")
    elif p < 0 or p > 1:
        raise ValueError("Probability should be greater than 0 and lower than 1.")
    elif n < k:
        raise ValueError("n should be lower than k.")"""


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
    count_mult = "do zrobienia"
    constant = exp_by_squaring(1-p, n)
    for i in range(0, k+1):
        prob += binomial_coeff(n, i) * (p/(1-p))**i
    prob *= constant
    return (prob, count_mult)


print(probability(8,3,0.5))


