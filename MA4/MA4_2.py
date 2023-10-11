#!/usr/bin/env python3

from person import Person
from numba import njit
import time
import matplotlib.pyplot as plt

@njit
def fib_numba(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
    
def fib_py(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_py(n - 1) + fib_py(n - 2)

n_values = list(range(30, 46))
py_times = []
numba_times = []
cpp_times = []

for n in n_values:
    start_time = time.perf_counter()
    fib_py(n)
    py_times.append(time.perf_counter() - start_time)

    start_time = time.perf_counter()
    fib_numba(n)
    numba_times.append(time.perf_counter() - start_time)


def main():
	f = Person(5)
	print(f.get())
	f.set(9)
	print(f.get())
	
if __name__ == '__main__':
	main()
