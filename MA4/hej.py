#!/usr/bin/env python3
from person import Person
from numba import njit

import time
import matplotlib.pyplot as plt

import ctypes
lib = ctypes.cdll.LoadLibrary('./libperson.so')

n=5

f=Person(n)
f.fib()