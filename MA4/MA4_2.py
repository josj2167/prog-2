#!/usr/bin/env python3

from person import Person
import time
from numba import njit
import matplotlib as plt

def fib_py(n):
    if n <= 1:
        return n
    else:
        return(fib_py(n - 1) + fib_py(n - 2))
    
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
	n_values = list(range(30,46))
	fib_py_times = []
	fib_numba_times = []
	fib_rec_times = []
	
	for n in n_values:
		start_time = time.perf_counter()
		result = fib_py(n)
		end_time = time.perf_counter()
		fib_py_times.append(end_time - start_time)

		start_time = time.perf_counter()
		result = fib_numba(n)
		end_time = time.perf_counter()
		fib_numba_times.append(end_time - start_time)
    
		f = Person(n)
		start_time = time.perf_counter()
		result = Person.fib(f, n)
		end_time = time.perf_counter()
		fib_rec_times.append(end_time - start_time)
    
	plt.figure(figsize=(10, 6))
	plt.plot(n_values, fib_py_times, label='fib_py')
	plt.plot(n_values, fib_numba_times, label='fib_numba')
	plt.plot(n_values, fib_rec_times, label='fib_rec')
	plt.xlabel('N Value')
	plt.ylabel('Execution Time (seconds)')
	plt.title('Fibonacci Execution Times')
	plt.legend()

	# Save the plot as a PNG image
	plt.savefig('fibonacci_execution_times.png')