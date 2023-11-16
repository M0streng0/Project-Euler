#!/usr/bin/python3
from itertools import permutations

def main():
    digits = '0123456789'

    all_permutations = permutations(digits)
    all_permutations_list = list(all_permutations)

    solution = all_permutations_list[1000000-1]
    print(''.join(solution))

if __name__ == '__main__':
    main()