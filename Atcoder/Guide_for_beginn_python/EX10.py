N = int(input())

A = list(map(int, input().split()))
sum = 0
for i in range(N):
    sum += A[i]
average = sum // N
for i in range(N):
    value = A[i] - average
    if value < 0:
        print(value * (-1))
    else:
        print(value)