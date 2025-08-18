N, Q = map(int,input().split())
A = list(map(int, input().split()))
B = [int(input()) for _ in range(Q)]

total_A = sum(A)
A_max = max(A)

for b in B:
    if b > A_max:
        value = b + (total_A - A_max)
    else:
        value = B
    if value > total_A:
        print(-1)
    else:
        print(value)