#!/usr/bin/python3
def openfile():
    raw = open('names.txt', 'rt').read()
    raw = raw.replace('\"','').replace(',',' ')
    names = raw.split()
    names.sort()
    return names

def main():
    file = openfile()
    num_word = 1
    output = 0
    for words in file:
        sum_letters = 0
        for letters in words:
            sum_letters += ord(letters) - 64
        output += sum_letters * num_word
        num_word += 1
    return output

if __name__ == '__main__':
    output = main()
    print(output)