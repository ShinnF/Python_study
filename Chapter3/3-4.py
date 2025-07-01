import math

def heron(a, b, c):
    s = 0.5 * (a + b + c)
    return math.sqrt(s * (s - a) * (s - b) * (s - c))
print (heron(3, 4, 5))