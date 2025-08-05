N = int(input())
T = list(map(int, input().split()))

min_val = min(T)
for i in range(N):
    if T[i] == min_val:
        print(i + 1)
        break