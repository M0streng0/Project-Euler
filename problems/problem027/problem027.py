#!/usr/bin/python3
import math
 
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def product(a,b):
    n = 1
    while is_prime(n ** 2 + a * n + b):
        n += 1
    return n

def main():
    highest_value = 0
    highest_a = 0
    highest_b = 0
    for a in range(-1000,1000):
        for b in range (-1001, 1001):
            value = product(a,b)
            if value > highest_value:
                highest_value = value
                highest_a = a
                highest_b = b
    print(f'Product of {highest_a} and {highest_b} is : {highest_a*highest_b}.\nThose 2 coefficients produces {product(highest_a,highest_b)} primes.')

if __name__ == '__main__':
    main()