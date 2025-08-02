MOD = 998244353

def modinv(x):
    return pow(x, MOD - 2, MOD)

N, M = map(int, input().split())
E = [1] * N

for _ in range(M):
    L, R = map(int, input().split())
    L -= 1
    R -= 1
    total = sum (E[L:R + 1]) % MOD
    length = R - L + 1
    avg = total * modinv(length) % MOD
    for i in range(L, R + 1):
        E[i] = avg
print(*E)