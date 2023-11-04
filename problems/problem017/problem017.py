#!/usr/bin/python3
def number_to_words(n):
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
            "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    if 1 <= n < 20:
        return ones[n]
    elif 20 <= n < 100:
        return tens[n // 10] + ones[n % 10]
    elif 100 <= n < 1000:
        return ones[n // 100] + "hundred" + ("and" + number_to_words(n % 100) if n % 100 != 0 else "")
    elif n == 1000:
        return "onethousand"
    else:
        return ""

def count_letters_in_words():
    total_letters = 0
    for i in range(1, 1001):
        word = number_to_words(i)
        total_letters += len(word)
    return total_letters

if __name__ == '__main__':
    total_letters_used = count_letters_in_words()
    print(total_letters_used)