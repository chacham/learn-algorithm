from collections import deque

def solve(R, C, LAND):
    res = 0
    for row in range(R):
        for col in range(C):
            if not LAND[row][col]:
                continue
            visited = [[-1] * C for _ in range(R)]
            q = deque([(row, col, 0)])
            while q:
                r, c, d = q.popleft()
                if r < 0 or r >= R or c < 0 or c >= C or not LAND[r][c]:
                    continue
                if visited[r][c] != -1 and visited[r][c] <= d:
                    continue
                visited[r][c] = d
                q.append((r+1, c, d+1))
                q.append((r-1, c, d+1))
                q.append((r, c+1, d+1))
                q.append((r, c-1, d+1))
            res = max(res, max(map(max, visited)))
    return res

if __name__ == "__main__":
    R, C = map(int, input().split())
    LAND = [[True if c == 'L' else False for c in input()] for _ in range(R)]
    print(solve(R, C, LAND))
