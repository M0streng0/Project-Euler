#!/usr/bin/python3
import math

def count_divisors(n):
    divisors = 0
    sqrt_n = int(math.sqrt(n))
    for i in range(1, sqrt_n + 1):
        if n % i == 0:
            divisors += 2  # Count both divisors i and n/i
    if sqrt_n * sqrt_n == n:
        divisors -= 1  # Correct for double-counting the square root
    return divisors

def find_triangle_number_with_divisors(target_divisors):
    num = 1
    triangle_number = 1
    while True:
        num += 1
        triangle_number += num
        divisors = count_divisors(triangle_number)
        if divisors > target_divisors:
            return triangle_number

if __name__ == '__main__':
    target_divisors = 500
    result = find_triangle_number_with_divisors(target_divisors)
    print(result)
