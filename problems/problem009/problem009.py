#!/usr/bin/python3

# a = m² - n²
# b = 2 * m * n
# c = m² + n²

# m² - n² + 2 * m * n + m² + n² = 1000
# 2m² + 2mn = 1000
# m² + mn = 500

for m in range(1, 500):
    for n in range(1, m):
        if m**2 + m*n == 500:
            product = (m**2 - n**2) * (2 * m * n) * (m**2 + n**2)
            print(product)