N, Q = map(int,input().split())
A = list(map(int, input().split()))
B = [int(input()) for _ in range(Q)]

total_A = sum(A)

for B_value in B:
    can_win = False
    for a_i in A:
        if a_i >= B:
            can_win = True
            break

    if not can_win:
        print(-1)
        continue

    S = 0
    for a_i in A:
        S += min(a_i, B - 1)

    x = S + 1
    if x > total_A:
        print(-1)
    else:
        print(x)