#!/usr/bin/python3
def fibonacci_sequence(digits):
    sequence = [0, 1]
    index = 2
    while True:
        next_number = sequence[-1] + sequence[-2]
        if len(str(next_number)) >= digits:
            break
        sequence.append(next_number)
        index += 1

    return index

def main():
    print(fibonacci_sequence(1000))

if __name__ == '__main__':
    main()