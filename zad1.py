import numpy as np
from scipy import linalg
import time
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def check_time(n):
    matrix = np.random.randint(low=-100, high=100, size=(n, n))
    vector = np.random.randint(low=-100, high=100, size=n)
    start_time = time.time()
    linalg.solve(matrix, vector)
    return time.time() - start_time


def plot_times(n, step):
    x = list(range(0, n, step))
    y = [check_time(i) for i in x]
    plt.plot(x, y, 'm.')
    plt.xlabel("Number of unknowns")
    plt.ylabel("Time of solution")
    plt.title("Complexity of calculations")
    plt.grid()
    plt.show()


def func(x, a, b, c):
    return a*x**2 + b*x + c


def find_factors(n, step):
    x = list(range(0, n, step))
    y = [check_time(i) for i in x]
    popt, pcov = curve_fit(func, x, y)
    a = popt[0]
    b = popt[1]
    c = popt[2]
    return [a, b, c]


def check(n, step):
    a = find_factors(n, step)[0]
    b = find_factors(n, step)[1]
    c = find_factors(n, step)[2]
    print(find_factors(n, step))
    x = np.arange(0, n)
    plt.plot(x, func(x, a, b, c))
    plot_times(n, step)
    plt.show()


print(check(5000, 300))

#https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.curve_fit.html
