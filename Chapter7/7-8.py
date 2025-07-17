def reverse_totuple(ln):
    value = tuple(reversed(ln))
    return value

print(reverse_totuple([1, 2, 3, 4, 5]) == (5, 4, 3, 2, 1))