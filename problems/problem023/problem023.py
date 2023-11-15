#!/usr/bin/python3
def is_abundant(number):
    divisors_sum = 1
    sqrt_number = int(number**0.5)

    for i in range(2, sqrt_number + 1):
        if number % i == 0:
            divisors_sum += i
            if i != number // i:
                divisors_sum += number // i

    return divisors_sum > number

def calculate_sums(abundant_numbers, limit):
    abundant_sums = [False] * (limit + 1)

    for i in range(len(abundant_numbers)):
        for j in range(i, len(abundant_numbers)):
            abundant_sum = abundant_numbers[i] + abundant_numbers[j]
            if abundant_sum <= limit:
                abundant_sums[abundant_sum] = True

    return abundant_sums

def main():
    limit = 28123
    abundant_numbers = [num for num in range(12, limit + 1) if is_abundant(num)]
    abundant_sums = calculate_sums(abundant_numbers, limit)

    non_abundant_sum = sum(i for i in range(limit + 1) if not abundant_sums[i])
    return non_abundant_sum

if __name__ == '__main__':
    output = main()
    print(output)