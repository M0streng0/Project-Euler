#!/usr/bin/python3

largest_palindrome = 0
for a in range(100, 1000):
    for b in range(100, 1000):
        product = a * b
        if (str(product) == str(product)[::-1]) and (product > largest_palindrome):
            largest_palindrome = product

print(largest_palindrome)