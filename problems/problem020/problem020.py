#!/usr/bin/python3
import math

def main(num):
    factorial = math.factorial(num)
    sum_digits = 0
    for digit in str(factorial):
        sum_digits += int(digit)
    return sum_digits

if __name__ == '__main__':
    number = 100
    print(main(number))