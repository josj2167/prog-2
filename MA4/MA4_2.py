#!/usr/bin/env python3

from person import Person
import time
from numba import njit

def fib_py(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_py(n - 1) + fib_py(n - 2)
    
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

if __name__ == '__main__':
    start_time = time.perf_counter()
    result = fib_py(30)
    end_time = time.perf_counter()
    print(f"Result (fib_py): {result}")
    print(f"Execution Time (fib_py): {end_time - start_time} seconds")

    start_time = time.perf_counter()
    result = fib_numba(30)
    end_time = time.perf_counter()
    print(f"Result (fib_numba): {result}")
    print(f"Execution Time (fib_numba): {end_time - start_time} seconds")
    
    start_time = time.perf_counter()
    result = Person.fib(Person, 30)
    end_time = time.perf_counter()
    print(f"Result (fib_rec): {result}")
    print(f"Execution Time (fib_rec): {end_time - start_time} seconds")
    

