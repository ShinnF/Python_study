h, w = map(int, input().split())
grid = [list(input()) for _ in range(h)]

for i in range(h):
    j = 0
    while j < w - 1:
        if grid[i][j] == 'T' and grid[i][j + 1] == 'T':
            grid[i][j] = 'P'
            grid[i][j + 1] = 'C'
            j += 1
        else:
            j += 1

for row in grid:
    print("".join(row))