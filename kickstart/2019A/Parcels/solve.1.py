from collections import deque

def solve(R, C, world):
    def maxDistance(d):
        maxD = -1
        for row in d:
            maxD = max(maxD, max(row))
        return maxD

    distance = [[123456789 for _ in range(C)] for _ in range(R)]
    for row, col in [(row, col) for row in range(R) for col in range(C)]:
        if world[row][col]:
            q = deque([(row, col, 0)])
            while q:
                r, c, d = q.popleft()
                if r < 0 or r >= R or c < 0 or c >= C:
                    continue
                if distance[r][c] > d:
                    distance[r][c] = d
                    q.append((r+1, c, d+1))
                    q.append((r-1, c, d+1))
                    q.append((r, c+1, d+1))
                    q.append((r, c-1, d+1))
    
    result = maxDistance(distance)
    distanceMaxToMin = sorted([(distance[row][col], row, col) for row in range(R) for col in range(C)], reverse=True)
    reduced = -1
    for d, row, col in distanceMaxToMin:
        if d <= reduced:
            break
        newDistance = [[d for d in row] for row in distance]
        q = deque([(row, col, 0)])
        while q:
            r, c, d = q.popleft()
            if r < 0 or r >= R or c < 0 or c >= C:
                continue
            if newDistance[r][c] > d:
                newDistance[r][c] = d
                q.append((r+1, c, d+1))
                q.append((r-1, c, d+1))
                q.append((r, c+1, d+1))
                q.append((r, c-1, d+1))
        newResult = maxDistance(newDistance)
        if newResult < result:
            reduced = result - newResult
            result = newResult
    return result

if __name__ == "__main__":
    T = int(input())
    for t in range(T):
        R, C = map(int, input().split())
        world = [[int(n) for n in input()] for _ in range(R)]
        print("Case #{}: {}".format(t+1, solve(R, C, world)))
