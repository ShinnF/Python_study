import math
def det(a, b, c):
    return b * b - 4 * a * c
def solution1(a, b, c):
    return (-b - math.sqrt(det(a, b, c))) / (a * 2)
def solution2(a, b, c):
    return (-b + math.sqrt(det(a, b, c))) / (a * 2)

print(det(1, -2, 1) == 0)
print(det(1, -5, 6) == 1)
def check_similar(x, y):
    print(abs(x - y) < 0.000001)
check_similar(solution1(1, -2, 1), 1.0) 