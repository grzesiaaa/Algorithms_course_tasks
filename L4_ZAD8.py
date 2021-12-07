from L4_ZAD5 import UnorderedList
import time
import matplotlib.pyplot as plt
import numpy as np

def make_plots(n, times1, times2, title1, title2):
    x1 = np.linspace(0, n)
    un_list_times = times1 * x1
    plt.subplot(2, 1, 1)
    plt.plot(x1, un_list_times, 'm.')
    plt.ylim(0, n / 10)
    plt.title(title1)
    plt.xlabel("Number of elements")
    plt.ylabel("Time")
    plt.grid()

    x2 = np.linspace(0, n)
    list_times = times2 * x2
    plt.subplot(2, 1, 2)
    plt.plot(x2, list_times, 'b.')
    plt.ylim(0, n / 10)
    plt.title(title2)
    plt.xlabel("Number of elements")
    plt.ylabel("Time")
    plt.grid()

    plt.tight_layout()
    plt.show()

def count_append_time(n):
    un_list = UnorderedList()
    list = []

    start1 = time.time()
    for i in range(0, n):
        un_list.append(i)
    end1 = time.time() - start1

    start2 = time.time()
    for i in range(0, n):
        list.append(i)
    end2 = time.time() - start2

    return end1, end2

def compare_append(n):
    make_plots(n, count_append_time(n)[0],
               count_append_time(n)[1],
               "Append method on Unordered List",
               "Append method on python list")


def count_insert_time(n):
    un_list = UnorderedList()
    for i in range(1, 6):
        un_list.append(i)
    list = [1, 2, 3, 4, 5]

    start1 = time.time()
    for i in range(0, n):
        un_list.insert(3, i)
    end1 = time.time() - start1

    start2 = time.time()
    for i in range(0, n):
        list.insert(3, i)
    end2 = time.time() - start2

    return end1, end2

def compare_insert(n):
    make_plots(n, count_insert_time(n)[0],
               count_insert_time(n)[1],
               "Insert method on Unordered List",
               "Insert method on python list")


def count_pop_time(n):
    un_list = UnorderedList()
    list = []
    for i in range(0, n):
        un_list.append(i)
        list.append(i)

    start1 = time.time()
    for _ in range(0, n):
        un_list.pop()
    end1 = time.time() - start1

    start2 = time.time()
    for _ in range(0, n):
        list.pop()
    end2 = time.time() - start2

    return end1, end2

def compare_pop(n):
    make_plots(n, count_pop_time(n)[0],
               count_pop_time(n)[1],
               "Pop method on Unordered List",
               "Pop method on python list")


def count_add_time(n):
    un_list = UnorderedList()

    start1 = time.time()
    for i in range(0, n):
        un_list.add(i)
    end1 = time.time() - start1

    return end1

def check_add(n):
    x1 = np.linspace(0, n)
    un_list_times = count_add_time(n) * x1
    plt.plot(x1, un_list_times, 'm.')
    plt.ylim(0, n / 10)
    plt.title("Add method on Unordered List")
    plt.xlabel("Number of elements")
    plt.ylabel("Time")
    plt.grid()
    plt.show()

    