import time
from person import Person

def main():
    n = 30
    f = Person(n)


    start_time = time.perf_counter()
    result = f.fib(n)
    end_time = time.perf_counter()

    print(f"Fibonacci Result: {result}")
    print(f"Execution Time: {end_time - start_time} seconds")

if __name__ == '__main__':
    main()

