def solve(ROW, COL):
    visited = [[False for _ in range(COL)] for _ in range(ROW)]
    target = ROW * COL
    def helper(R, C, path):
        if len(path) == target:
            return True, path
        for r, c in [(row, col) for row in range(ROW) for col in range(COL)]:
            if visited[r][c] \
                    or abs(r - c) == abs(R - C) \
                    or r + c == R + C \
                    or r == R or c == C:
                continue
            path.append((r, c))
            visited[r][c] = True
            possible, path = helper(r, c, path)
            if possible:
                return possible, path
            path.pop()
            visited[r][c] = False
        return False, path

    for r, c in [(row, col) for row in range(ROW) for col in range(COL)]:
        # print(r, c)
        visited[r][c] = True
        possible, path = helper(r, c, [(r, c)])
        if possible:
            return (possible, path)
        visited[r][c] = False
    return False, None

if __name__ == "__main__":
    T = int(input())
    for t in range(T):
        R, C = map(int, input().split())
        possible, path = solve(R, C)
        if possible:
            print('Case #{}: POSSIBLE'.format(t+1))
            for r, c in path:
                print(r+1, c+1)
        else:
            print('Case #{}: IMPOSSIBLE'.format(t+1))
