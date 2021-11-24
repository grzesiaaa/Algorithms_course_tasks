from L4_ZAD1 import QueueBaE, QueueBaB
import time
import matplotlib.pyplot as plt

def compare_implementations(n):
    BaB = QueueBaB()
    BaE = QueueBaE()

    start1 = time.time()
    for _ in range(0,1000):
        for i in range(0, n):
            BaB.enqueue(i)
    time1 = (time.time()-start1)/1000

    start2 = time.time()
    for _ in range(0, 1000):
        for i in range(0, n):
            BaE.enqueue(i)
    time2 = (time.time()-start2)/1000

    start3 = time.time()
    for _ in range(0,1000):
        for _ in range(0, n):
            BaB.dequeue()
    time3 = (time.time()-start3)/1000

    start4 = time.time()
    for _ in range(0, 1000):
        for _ in range(0, n):
            BaE.dequeue()
    time4 = (time.time() - start4) / 1000

    times = [time1, time2, time3, time4]

    return times

def plots(n):

    for _ in range(0, n):
        print(compare_implementations(n))
    plt.plot(n, compare_implementations())
print(plots(10))



