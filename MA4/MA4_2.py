#!/usr/bin/env python3

from person import Person

def main():
	f = Person(5)
	print(f.get())
	f.set(8)
	print(f.get())

if __name__ == '__main__':
	main()
