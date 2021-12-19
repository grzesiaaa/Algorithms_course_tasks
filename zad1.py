import numpy as np
from scipy import linalg
import random
import time
import matplotlib.pyplot as plt


def lala(n):
    matrices =[]
    vectors = []

    for i in range(1,n+1):
        a = [[random.randint(-100, 100) for col in range(i)] for row in range(i)]
        b = [random.randint(-100, 100) for col in range(i)]
    a = np.array(a)
    b = np.array(b)
    print(a)
    print(b)
    x = linalg.solve(a,b)
    print(x)
    return np.dot(a,x) == b


print(lala(3))
"""a = np.array([[10,2,1],
 [ 8,10,2],
 [1,2,3]])
b= np.array([8,1,3])
x = linalg.solve(a,b)
print(x)
print(np.dot(a,x) ==b)"""