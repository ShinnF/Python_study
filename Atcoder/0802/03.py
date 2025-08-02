N = int(input())
A = list(map(int, input().split()))

count = {}
for i in range(N):
    key = i + A[i]
    if key in count:
        count[key] += 1
    else:
        count[key] = 1

ans = 0
for j in range(N):
    key = j - A[j]
    if key in count:
        ans += count[key]

print(ans)