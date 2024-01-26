#!/usr/bin/python3
def solution(denominator):
    n = 1 % denominator
    if n == 0:
        return 0

    mem = {}
    n *= 10
    pos = 0

    while True:
        pos += 1
        n = n % denominator
        if n == 0:
            return 0
        if n in mem:
            i = mem[n]
            return pos - i
        else:
            mem[n] = pos
        n *= 10

def decimal(digits):
    d = 2
    highest_value = 1
    highest_denominator = 2
    while d < digits:
        calc = solution(d)
        if calc > highest_value:
            highest_value = calc
            highest_denominator = d
        d += 1
    return highest_value, highest_denominator

def main():
    print(decimal(1000))

if __name__ == '__main__':
    main()