import numpy as np
from scipy import linalg
import random
import time
import matplotlib.pyplot as plt


def lala(n):
    matrices = []
    vectors = []

    for i in range(1, n+1):
        matrices = [[random.randint(-100, 100) for col in range(i)] for row in range(i)]
        vectors = [random.randint(-100, 100) for col in range(i)]

    a = np.array(matrices)
    b = np.array(vectors)
    print(a)
    print(b)
    start_time = time.time()
    x = linalg.solve(a, b)
    fin_time = time.time() - start_time
    # print(x)
    return fin_time


print(lala(300))
