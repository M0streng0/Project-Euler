#!/usr/bin/python3

def is_prime(num):
    for i in range(2,num):
        if (num % i) == 0:
            return False
    return True

i = 1
num = 2
while i <= 6:
    if is_prime(num):
        i += 1
    num += 1
print(num - 1)