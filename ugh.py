import numpy as np
from scipy import linalg
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import time


def check_time(n):
    matrix = np.random.randint(low=-100, high=100, size=(n, n))
    vector = np.random.randint(low=-100, high=100, size=n)
    start_time = time.time()
    linalg.solve(matrix, vector)
    return time.time() - start_time


def plot_times():
    x = []
    for k in range(9, 15):
        x.append(2**k)
    y = [check_time(i) for i in x]
    plt.plot(x, y, 'm.')
    plt.xlabel("Number of unknowns")
    plt.ylabel("Time of solution")
    plt.title("Complexity of calculations")
    plt.grid()
    plt.show()

def plot_log():
    x = []
    for k in range(9, 15):
        x.append(2 ** k)
    y = [check_time(i) for i in x]
    plt.loglog(x, y, 'g.')
    plt.show()


def func(x, a, b):
    return a*(x**b)


def find_factors():
    x = []
    for k in range(9, 15):
        x.append(2 ** k)
    y = [check_time(i) for i in x]
    popt, pcov = curve_fit(func, x, y)
    a = popt[0]
    b = popt[1]
    return [a, b]

def check():
    a = find_factors()[0]
    b = find_factors()[1]
    print(find_factors())
    x = np.arange(2**9, 2**15)
    plt.plot(x, func(x, a, b))
    plot_times()
    plt.show()

