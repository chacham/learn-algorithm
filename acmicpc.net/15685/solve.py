direction = [[1, 0], [0, -1], [-1, 0], [0, 1]]

def dragon_curve(dir, g):
    if g == 0:
        return [dir]
    head = dragon_curve(dir, g-1)
    tail = [[y, -x] for (x, y) in reversed(head)]
    return head + tail

def solve(curves):
    grid = [[0] * 101 for _ in range(101)]
    for x, y, d, g in curves:
        curve = dragon_curve(direction[d], g)
        grid[x][y] = 1
        for dx, dy in curve:
            x += dx
            y += dy
            grid[x][y] = 1
    res = 0
    for x in range(100):
        for y in range(100):
            res += grid[x][y] and grid[x+1][y] and grid[x][y+1] and grid[x+1][y+1]
    return res

if __name__ == "__main__":
    N = int(input())
    curves = []
    for _ in range(N):
        x, y, d, g = map(int, input().split())
        curves.append([x, y, d, g])
    print(solve(curves))

