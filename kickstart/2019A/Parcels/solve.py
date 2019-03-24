from collections import deque

def solve(R, C, world):
    distance = [[float('inf') for _ in range(C)] for _ in range(R)]
    for row in range(R):
        for col in range(C):
            if world[row][col]:
                distance[row][col] = 0
            else:
                dist = 123456789
                if row > 0:
                    dist = min(dist, distance[row-1][col] + 1)
                if row < R - 1:
                    dist = min(dist, distance[row+1][col] + 1)
                if col > 0:
                    dist = min(dist, distance[row][col-1] + 1)
                if col < C - 1:
                    dist = min(dist, distance[row][col+1] + 1)
                distance[row][col] = dist
    for row in reversed(range(R)):
        for col in reversed(range(C)):
            if world[row][col]:
                distance[row][col] = 0
            else:
                dist = 123456789
                if row > 0:
                    dist = min(dist, distance[row-1][col] + 1)
                if row < R - 1:
                    dist = min(dist, distance[row+1][col] + 1)
                if col > 0:
                    dist = min(dist, distance[row][col-1] + 1)
                if col < C - 1:
                    dist = min(dist, distance[row][col+1] + 1)
                distance[row][col] = dist
    
    result = float('-inf')
    for row in range(R):
        for col in range(C):
            result = max(result, distance[row][col])

    for row in range(R):
        for col in range(C):
            newDistance = [[float('inf') for _ in range(C)] for _ in range(R)]
            if not world[row][col]:
                q = deque([(row, col, 0)])
                while q:
                    # print(q)
                    r, c, d = q.popleft()
                    if r < 0 or r >= R or c < 0 or c >= C:
                        continue
                    if min(newDistance[r][c], distance[r][c]) <= d:
                        continue
                    newDistance[r][c] = d
                    q.append((r+1, c, d+1))
                    q.append((r-1, c, d+1))
                    q.append((r, c+1, d+1))
                    q.append((r, c-1, d+1))
                tmpRes = float('-inf')
                for r, c in [(r, c) for r in range(R) for c in range(C)]:
                    tmpRes = max(tmpRes, min(distance[r][c], newDistance[r][c]))
                result = min(tmpRes, result)
    return result

if __name__ == "__main__":
    T = int(input())
    for t in range(T):
        R, C = map(int, input().split())
        world = [[int(n) for n in input()] for _ in range(R)]
        print("Case #{}: {}".format(t+1, solve(R, C, world)))
