#!/usr/bin/python3
def main(num):
    power = 2 ** num
    digits = 0
    for i in str(power):
        digits += int(i)
    return(digits)

if __name__ == '__main__':
    number = 1000
    output = main(number)
    print(output)