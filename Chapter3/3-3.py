def feet_to_cm(f, i):
    return f * 30.48 + (i / 12 * 30.48)
def check_similar(x,y):
    print(abs(x-y) < 0.000001)
check_similar(feet_to_cm(5, 2), 157.48)
check_similar(feet_to_cm(6, 5), 195.58)

def quadaratic(a, b, c, x):
    return a * x ** 2 + b * x + c
print(quadaratic(1, 2, 1, 3) == 16)
print(quadaratic(1, -5, -2, 7) == 12) 