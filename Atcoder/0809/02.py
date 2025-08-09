S = input()

max_value = 0.0
for i in  range(len(S)):
    for j in range(i, len(S)):
        t = S[i:j + 1]
        t_len = len(t)

        if t_len >= 3 and t.startswith('t') and t.endswith('t'):
            t_count = t.count('t')
            value = (t_count - 2) / (t_len - 2)

            if value > max_value:
                max_value = value

print(max_value)