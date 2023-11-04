#!/usr/bin/python3
import math

# Routes = (m + n)! / (m! * n!)
# Routes = 40! / (20! * 20!), m = n = 20

def calculate_routes(m, n):
    return math.factorial(m + n) // (math.factorial(m) * math.factorial(n))

if __name__ == '__main__':
    grid_size = 20
    routes = calculate_routes(grid_size, grid_size)
    print(routes)