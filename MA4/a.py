import time

def fib(n):
    if n <= 1:
        return n
    else:
        return(fib(n - 1) + fib(n - 2))

n_values = list(range(30, 46))

for n in n_values:
    start_time = time.time()
    result = fib(n)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"n={n}, result={result}, time={elapsed_time} seconds")