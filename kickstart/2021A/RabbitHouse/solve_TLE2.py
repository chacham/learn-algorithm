from collections import deque

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def solve(R, C, MAP):
    q = deque([(r, c) for r in range(R) for c in range(C)])
    res = 0
    while q:
        r, c = q.popleft()
        v = MAP[r][c]
        maxD = 0
        for i in range(4):
            br = r + dr[i]
            bc = c + dc[i]
            if 0 <= br < R and 0 <= bc < C:
                maxD = max(maxD, MAP[br][bc] - v)
        if maxD > 1:
            MAP[r][c] += maxD - 1
            res += maxD - 1
            for i in range(4):
                br = r + dr[i]
                bc = c + dc[i]
                if 0 <= br < R and 0 <= bc < C:
                    q.append((br, bc))
    return res

if __name__ == "__main__":
    T = int(input())
    for t in range(T):
        R, C = map(int, input().split())
        MAP = [[int(x) for x in input().split()] for _ in range(R)]
        print(f"Case #{t+1}: {solve(R, C, MAP)}")
