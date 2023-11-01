#!/usr/bin/python3

sum_squares = 0
sum_numbs = 0
for i in range(1,101):
    sum_squares += (i * i)
    sum_numbs += i
square_sum_numbs = (sum_numbs * sum_numbs)
difference = square_sum_numbs - sum_squares
print(difference)