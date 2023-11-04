#!/usr/bin/python3
def collatz_sequence_length(num):
    length = 1
    while num != 1:
        if num % 2 == 0:
            num /= 2
        else:
            num = 3 * num + 1
        length += 1
    return length

def find_longest_collatz_sequence(limit):
    max_length = 0
    starting_number = 0

    for i in range(1, limit):
        length = collatz_sequence_length(i)
        if length > max_length:
            max_length = length
            starting_number = i

    return starting_number

if __name__ == '__main__':
    limit = 1000000
    result = find_longest_collatz_sequence(limit)
    print(result)