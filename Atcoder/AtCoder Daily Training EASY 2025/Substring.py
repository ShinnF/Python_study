def count_unique_substrings(S):
    substrings = set()
    n = len(S)
    for i in range(n):
        for j in range(i + 1, n + 1):
            substrings.add(S[i:j])
    return len(substrings)

S = input().strip()
print(count_unique_substrings(S))