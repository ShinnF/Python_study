Q = int(input())

bag = []
output = []

for _ in range(Q):
    query = input().split()
    if query[0] == '1':
        x = int(query[1])
        bag.append(x)
    else:
        smallest = min(bag)
        bag.remove(smallest)
        output.append(smallest)

for ans in output:
    print(ans)