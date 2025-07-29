value = int(input())
i = 0
sum = 0

while i < value:
    A, B = map(int, input().split())
    sum = A + B
    print(sum)
    i += 1