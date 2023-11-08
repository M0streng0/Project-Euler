#!/usr/bin/python3
def sumOfDiv(x): 
    divisors_sum = 1
    for i in range(2, x // 2 + 1):
        if x % i == 0: 
            divisors_sum += i 
    return divisors_sum

def isAmicable(a, b): 
    return sumOfDiv(a) == b and sumOfDiv(b) == a

def main():
    amicable_numbers = []
    for a in range(2, 10000):
        b = sumOfDiv(a)
        if a != b and isAmicable(a, b):
            amicable_numbers.extend([a, b])
    
    unique_amicable_numbers = list(set(amicable_numbers))
    print(sum(unique_amicable_numbers))

if __name__ == '__main__':
    main()