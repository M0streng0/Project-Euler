#!/usr/bin/python3

a, b = 1, 2
even_sum = 0
while a < 4000000:
	if (a % 2 == 0):
		even_sum += a
	a, b = b, a + b
print(even_sum)