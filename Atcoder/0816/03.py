N = int(input())
R, C = [], []

for _ in range(N):
    r, c = map(int, input().split())
    R.append(r)
    C.append(c)

rmin, rmax = min(R), max(R)
cmin, cmax = min(C), max(C)

ans = max(rmax - rmin, cmax - cmin)
print((ans + 1) // 2)