def countIslands(N, MAP, H):
    visited = [[False] * N for _ in range(N)]
    stack = []
    res = 0
    for r in range(N):
        for c in range(N):
            if MAP[r][c] > H and not visited[r][c]:
                res += 1
                stack.append((r, c))
            while stack:
                row, col = stack.pop()
                if row < 0 or row >= N or col < 0 or col >= N or visited[row][col] or MAP[row][col] <= H:
                    continue
                visited[row][col] = True
                stack.append((row-1, col))
                stack.append((row+1, col))
                stack.append((row, col-1))
                stack.append((row, col+1))
    return res

if __name__ == "__main__":
    N = int(input())
    MAP = [[int(x) for x in input().split()] for _ in range(N)]
    res = 1
    for h in range(1, 100):
        res = max(res, countIslands(N, MAP, h))
    print(res)
