from L4_ZAD1 import QueueBaE, QueueBaB
import time
import matplotlib.pyplot as plt
import numpy as np

def count_times(n):
    BaB = QueueBaB()
    BaE = QueueBaE()

    start1 = time.time()
    for i in range(0, n):
        BaB.enqueue(i)
    time1 = time.time()-start1

    start2 = time.time()
    for i in range(0, n):
        BaE.enqueue(i)
    time2 = time.time()-start2

    start3 = time.time()
    for _ in range(0, n):
        BaB.dequeue()
    time3 = time.time()-start3

    start4 = time.time()
    for _ in range(0, n):
        BaE.dequeue()
    time4 = time.time() - start4

    times = [time1, time2, time3, time4]
    return times


def compare_enqueue(n):
    x1 = np.linspace(0, n)
    BaB_enq = count_times(n)[0] * x1
    plt.subplot(2, 1, 1)
    plt.plot(x1, BaB_enq, 'm.')
    plt.ylim(0, n/2)
    plt.title("Enqueue method on QueueBaB")
    plt.xlabel("Number of elements")
    plt.ylabel("Time")
    plt.grid()

    x2 = np.linspace(0, n)
    BaE_enq = count_times(n)[1] * x2
    plt.subplot(2, 1, 2)
    plt.plot(x2, BaE_enq, 'b.')
    plt.ylim(0, n/2)
    plt.title("Enqueue method on QueueBaE")
    plt.xlabel("Number of elements")
    plt.ylabel("Time")
    plt.grid()

    plt.tight_layout()
    plt.show()

def compare_dequeue(n):
    x3 = np.linspace(0, n)
    BaB_deq = count_times(n)[2] * x3
    plt.subplot(2, 1, 1)
    plt.plot(x3, BaB_deq, 'm.')
    plt.ylim(0, n/2)
    plt.title("Dequeue method on QueueBaB")
    plt.xlabel("Number of elements")
    plt.ylabel("Time")
    plt.grid()

    x4 = np.linspace(0, n)
    BaE_deq = count_times(n)[3] * x4
    plt.subplot(2, 1, 2)
    plt.plot(x4, BaE_deq, 'b.')
    plt.ylim(0, n/2)
    plt.title("Dequeue method on QueueBaE")
    plt.xlabel("Number of elements")
    plt.ylabel("Time")
    plt.grid()

    plt.tight_layout()
    plt.show()




