import time
import matplotlib.pyplot as plt
from MA4_2 import fib_py
from MA4_2 import fib_numba
from person import Person

# Define the Fibonacci numbers you want to compute
n_values = [20, 25, 30, 35, 40]

# Initialize empty lists to store execution times
py_times = []
numba_times = []
cpp_times = []

# Measure execution times for Python, Numba, and C++ versions
for n in n_values:
    start_time = time.time()
    fib_py(n)
    py_times.append(time.time() - start_time)

    start_time = time.time()
    fib_numba(n)
    numba_times.append(time.time() - start_time)

    f = Person(n)
    start_time = time.time()
    f.fib_cpp()
    cpp_times.append(time.time() - start_time)

# Create a plot
plt.plot(n_values, py_times, label="Python")
plt.plot(n_values, numba_times, label="Numba")
plt.plot(n_values, cpp_times, label="C++")
plt.xlabel("Fibonacci Number (n)")
plt.ylabel("Execution Time (seconds)")
plt.legend()
plt.title("Execution Time for Fibonacci Calculation")
plt.grid(True)

# Save the plot to disk
plt.savefig("fibonacci_timing.png")

# Show the plot (optional)
plt.show()