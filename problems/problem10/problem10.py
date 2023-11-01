#!/usr/bin/python3

prime_numbs = [2,3,5,7]
def is_prime(num):
    for i in prime_numbs:
        if (num % i) == 0:
            return False
    if num < 1415: # 1415 is the sqrt of 2000000
        prime_numbs.append(num)
    return True

sum_values = 0
for i in range(2,2000001):
    if is_prime(i):
        sum_values += i
print(sum_values + 17)