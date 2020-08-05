def multiply_recursive(x, y):
    # to reduce number of recursion to avoid overflowing
    if x < y:
        return multiply_recursive(y, x)

    if y == 0:
        return 0
    else:
        return x + multiply_recursive(x, y - 1)


print(multiply_recursive(2, 6))
