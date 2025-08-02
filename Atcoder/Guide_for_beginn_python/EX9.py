N = int(input())
A = int(input())

for i in range(N):
    op, x = input().split()
    x = int(x)

    if op == "+":
        A += x
    elif op == "-":
        A -= x
    elif op == "*":
        A *= x
    elif op == "/" and x != 0:
        A /= x
    else:
        print("error")
        break
    print(i + 1, A)