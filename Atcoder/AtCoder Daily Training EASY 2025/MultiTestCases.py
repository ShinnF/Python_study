T = int(input())

for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    odd_count = sum(1 for x in A if x % 2 == 1)
    print(odd_count)