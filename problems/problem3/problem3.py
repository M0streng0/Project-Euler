#!/usr/bin/python3

i = 2
number = 600851475143
while i * i <= number:
	if number % i:
		i += 1
	else:
		number //= i
print(number)