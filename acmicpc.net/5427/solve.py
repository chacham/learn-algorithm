from collections import deque

def solve(W, H, MAP):
    visited = [[False] * W for _ in range(H)]

    def move(pos: deque):
        nextPos = deque()
        while pos:
            r, c = pos.popleft()
            if c < 0 or c >= W or r < 0 or r >= H:
                return True, nextPos
            if visited[r][c] or MAP[r][c] == '*' or MAP[r][c] == '#':
                continue
            visited[r][c] = True
            nextPos.append((r-1, c))
            nextPos.append((r+1, c))
            nextPos.append((r, c-1))
            nextPos.append((r, c+1))
        return False, nextPos

    def fire(fires: deque):
        nextFires = deque()
        while fires:
            r, c = fires.popleft()
            if c < 0 or c >= W or r < 0 or r >= H:
                continue
            if MAP[r][c] == '*' or MAP[r][c] == '#':
                continue
            MAP[r][c] = '*'
            nextFires.append((r-1, c))
            nextFires.append((r+1, c))
            nextFires.append((r, c-1))
            nextFires.append((r, c+1))
        return nextFires

    pos = deque()
    fires = deque()

    for r in range(H):
        for c in range(W):
            if MAP[r][c] == '@':
                pos.append((r, c))
            if MAP[r][c] == '*':
                MAP[r][c] = '.'
                fires.append((r, c))

    escaped = False
    res = -1
    while not escaped and pos:
        fires = fire(fires)
        escaped, pos = move(pos)
        res += 1
        # print(pos, fires)
        # print(*MAP, sep='\n', end='\n\n')

    return res if escaped else -1

if __name__ == "__main__":
    T = int(input())
    for t in range(T):
        W, H = map(int, input().split())
        MAP = [list(input()) for _ in range(H)]
        res = solve(W, H, MAP)
        if res == -1:
            print("IMPOSSIBLE")
        else:
            print(res)
