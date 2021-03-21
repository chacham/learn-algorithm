from collections import deque

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def solve(R, C, MAP):
    sortedPoints = sorted([(r, c, MAP[r][c]) for r in range(R) for c in range(C)], key=lambda x: x[2], reverse=True)
    Q = deque(sortedPoints)
    res = 0
    while Q:
        q = deque([Q.popleft()])
        while q:
            r, c, _ = q.popleft()
            v = MAP[r][c]
            for i in range(4):
                br = r + dr[i]
                bc = c + dc[i]
                if 0 <= br < R and 0 <= bc < C and v - MAP[br][bc] > 1:
                    res += v - MAP[br][bc] - 1
                    MAP[br][bc] = v - 1
                    q.append((br, bc, v-1))
    return res

if __name__ == "__main__":
    T = int(input())
    for t in range(T):
        R, C = map(int, input().split())
        MAP = [[int(x) for x in input().split()] for _ in range(R)]
        print(f"Case #{t+1}: {solve(R, C, MAP)}")
