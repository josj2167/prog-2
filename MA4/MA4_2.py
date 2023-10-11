#!/usr/bin/env python3

from person import Person
from numba import njit

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
	f = Person(5)
	print(f.get())
	f.set(8)
	print(f.get())

if __name__ == '__main__':
	main()
