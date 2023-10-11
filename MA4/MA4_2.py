#!/usr/bin/env python3

from person import Person
from numba import njit

import time
import matplotlib.pyplot as plt
from person import Person


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
    
def main():
    n_values_1 = list(range(30, 46))
    py_times_1 = []
    numba_times_1 = []
    cpp_times_1 = []

    for n in n_values_1:
        start_time = time.perf_counter()
        fib_py(n)
        py_times_1.append(time.perf_counter() - start_time)
        
        start_time = time.perf_counter()
        fib_numba(n)
        numba_times_1.append(time.perf_counter() - start_time)

        # Call the C++ code here and measure its execution time
        f = Person(n)
        start_time = time.perf_counter()
        f.fibonacci()
        cpp_times_1.append(time.perf_counter() - start_time)

    n_values_2 = list(range(20, 31))
    py_times_2 = []
    numba_times_2 = []

    for n in n_values_2:
        start_time = time.perf_counter()
        fib_py(n)
        py_times_2.append(time.perf_counter() - start_time)

        start_time = time.perf_counter()
        fib_numba(n)
        numba_times_2.append(time.perf_counter() - start_time)

    
    plt.figure(1)
    plt.plot(n_values_1, py_times_1, label='Python')
    plt.plot(n_values_1, numba_times_1, label='Numba')
    plt.plot(n_values_1, cpp_times_1, label='C++')
    plt.xlabel('n')
    plt.ylabel('Seconds')
    plt.legend()
    plt.savefig('fibonacci_timings_1.png')

    plt.figure(2)
    plt.plot(n_values_2, py_times_2, label='Python')
    plt.plot(n_values_2, numba_times_2, label='Numba')
    plt.xlabel('n')
    plt.ylabel('Seconds')
    plt.legend()
    plt.savefig('fibonacci_timings_2.png')

    # For the C++ code, you need to call it and measure its time for n = 47
    f = Person(47)
    start_time = time.perf_counter()
    f.fibonacci()
    cpp_time_47 = time.perf_counter() - start_time
    print(f"Fibonacci(47) using C++ took {cpp_time_47} seconds")


if __name__ == '__main__':
    main()