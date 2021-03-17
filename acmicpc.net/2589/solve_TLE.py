def solve(R, C, LAND):
    res = 0
    for row in range(R):
        for col in range(C):
            if not LAND[row][col]:
                continue
            visited = {}
            stack = [(row, col, 0)]
            while stack:
                r, c, d = stack.pop()
                if r < 0 or r >= R or c < 0 or c >= C or not LAND[r][c]:
                    continue
                if (r, c) in visited and visited[(r, c)] <= d:
                    continue
                visited[(r, c)] = d
                stack.append((r+1, c, d+1))
                stack.append((r-1, c, d+1))
                stack.append((r, c+1, d+1))
                stack.append((r, c-1, d+1))
            res = max(res, max(visited.values()))
    return res

if __name__ == "__main__":
    R, C = map(int, input().split())
    LAND = [[True if c == 'L' else False for c in input()] for _ in range(R)]
    print(solve(R, C, LAND))
