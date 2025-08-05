S = input()

answer = 1

for i in range(len(S)):
    if S[i] == "+":
        answer += 1
    if S[i] == "-":
        answer -= 1

print(answer)