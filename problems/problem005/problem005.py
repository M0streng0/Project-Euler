#!/usr/bin/python3

small_num = 20
divide = [11,12,13,14,15,16,17,18,19,20] # I don't need the other values (from 1-10)

def check(n):
    for values in divide:
        if n%values != 0:
            return False
        if values == 20 and n%values == 0:
            print(n)
            return True

while check(small_num) != True:
    small_num += 1