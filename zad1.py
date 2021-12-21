import numpy as np
from scipy import linalg
import time
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import math



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

    ratio = [None]*len(y)
    for i in range(1, len(y)):
        ratio[i] = y[i] / y[i - 1]
    lratio = [None]
    for val in ratio:
        if val:
            lratio.append(math.log(val, 2))
    print("{} \t {} \t {} \t {}".format("N", "T", "Ratio", "Log"))
    for i in range(len(y)):
        print("{} \t {} \t {} \t {}".format(x[i], y[i], ratio[i], lratio[i]))

#print(plot_times())


def func(x, a):
    return a*x**2


def find_factors():
    x = []
    for k in range(9, 15):
        x.append(2 ** k)
    y = [check_time(i) for i in x]
    popt, pcov = curve_fit(func, x, y)
    a = popt[0]
    return a


def check():
    a = find_factors()
    print(find_factors())
    x = np.arange(512, 2**15 + 1 )
    plt.plot(x, func(x, a))
    plot_times()
    plt.show()

#print(check())
#https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.curve_fit.html
