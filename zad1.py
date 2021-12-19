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

def lin_alg(n):
    matrices = []
    vectors = []

    for i in range(2, 21):
        a = [[random.randint(-50, 50) for col in range(i)] for row in range(i)]
        b = [random.randint(-50, 50) for col in range(i)]
        matrices.append(a)
        vectors.append(b)

    times = []  # measures time for .solve method

    for j in range(0, len(matrices)):
        print(len(matrices))
        x = []
        start_matrix = time.time()
        for i in range(0, n):
            print(str(linalg.det(matrices[j])))
            if (linalg.det(matrices[j]) == 0):
                print("Determinant equal 0")
            else:
                print("Determinant equal: " + str(linalg.det(matrices[j])))
                x.append(linalg.solve(matrices[j], vectors[j]))
                print(x[i])
                print("Result " + str(j + 2) + 'x' + str(j + 2))
                print(np.dot(matrices[j], x[i]) == vectors[j])
        end_matrix = time.time()
        times.append((end_matrix - start_matrix) / 100)
        print(times)

    # Creating the bar plot
    bars = []
    for i in range(0, len(times)):
        bars.append(str(i + 2) + "x" + str(i + 2))
        # print(times[i], end=" ")  #print for check times list
        # print(bars[i], end=" ")      # print for check bars list

    y_pos = np.arange(len(times))

    plt.figure(figsize=(20, 5))
    plt.grid()
    plt.bar(y_pos, times, color='#ffd700')
    plt.xticks(y_pos, bars)
    plt.xlabel('Matrix', fontsize=12, color='#323232')
    plt.ylabel('Time of solving', fontsize=12, color='#323232')
    plt.title('Times of solving matrices of different dimensions', fontsize=16, color='#323232')
    plt.show()


if __name__ == '__main__':
    lin_alg(100)
