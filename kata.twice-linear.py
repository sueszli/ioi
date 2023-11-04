# https://www.codewars.com/kata/5672682212c8ecf83e000050/python

# sequence u:
# - u(0) = 1
# - u_next = 2 * u_prev + 1
# - u_next = 3 * u_prev + 1

# u = (1, 3, 4, 7, 9, 10, 13, 15, 19, 21, 22, 27, ...)

# Task:
# Given parameter n, return the n'th element in the u sequence
# ie. u(10) should return 22


def dbl_linear(n):
    u = [1]
    x, y = 0, 0

    while len(u) <= n:
        x_val = 2 * u[x] + 1
        y_val = 3 * u[y] + 1
        if x <= y:
            x += 1
        if x >= y:
            y += 1
        u.append(min(x_val, y_val))

    return u[n]


arg = 10
result = dbl_linear(arg)
print(f"element index {arg} in the sequence is: {result}")
