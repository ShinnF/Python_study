N, M = map(int, input().split())

S_str = input()
T_str = input()

S = list(S_str)
T = list(T_str)

imos = [0] * (N + 1)

for _ in range(M):
    L, R = map(int, input().split())
    imos[L - 1] += 1
    imos[R] -= 1

imos_sum = 0
for i in range(N):
    imos_sum += imos[i]
    if imos_sum % 2 == 1:
        S[i], T[i] = T[i], S[i]

print("".join(S))