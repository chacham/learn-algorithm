def solve(R, C, MAP):
    lSeg = [[0] * C for _ in range(R)]
    uSeg = [[0] * C for _ in range(R)]
    rSeg = [[0] * C for _ in range(R)]
    dSeg = [[0] * C for _ in range(R)]

    lSeg[0][0] = MAP[0][0]
    uSeg[0][0] = MAP[0][0]
    rSeg[-1][-1] = MAP[-1][-1]
    dSeg[-1][-1] = MAP[-1][-1]
    for c in range(1, C):
        lSeg[0][c] = lSeg[0][c-1] + 1 if MAP[0][c] else 0
        uSeg[0][c] = MAP[0][c]
    for r in range(1, R):
        lSeg[r][0] = MAP[r][0]
        uSeg[r][0] = uSeg[r-1][0] + 1 if MAP[r][0] else 0
    for c in reversed(range(C-1)):
        rSeg[-1][c] = rSeg[-1][c+1] + 1 if MAP[-1][c] else 0
        dSeg[-1][c] = MAP[-1][c]
    for r in reversed(range(R-1)):
        rSeg[r][-1] = MAP[r][-1]
        dSeg[r][-1] = dSeg[r+1][-1] + 1 if MAP[r][-1] else 0
    
    for r in range(1, R):
        for c in range(1, C):
            lSeg[r][c] = lSeg[r][c-1] + 1 if MAP[r][c] else 0
            uSeg[r][c] = uSeg[r-1][c] + 1 if MAP[r][c] else 0
    for r in reversed(range(R-1)):
        for c in reversed(range(C-1)):
            rSeg[r][c] = rSeg[r][c+1] + 1 if MAP[r][c] else 0
            dSeg[r][c] = dSeg[r+1][c] + 1 if MAP[r][c] else 0

    # print(*uSeg, sep="\n", end="\n\n")
    # print(*dSeg, sep="\n", end="\n\n")
    # print(*lSeg, sep="\n", end="\n\n")
    # print(*rSeg, sep="\n", end="\n\n")
    res = 0
    for r in range(0, R):
        for c in range(0, C):
            res += max(min(uSeg[r][c] // 2, lSeg[r][c]) - 1, 0)
            res += max(min(uSeg[r][c], lSeg[r][c] // 2) - 1, 0)
            res += max(min(uSeg[r][c] // 2, rSeg[r][c]) - 1, 0)
            res += max(min(uSeg[r][c], rSeg[r][c] // 2) - 1, 0)
            res += max(min(dSeg[r][c] // 2, lSeg[r][c]) - 1, 0)
            res += max(min(dSeg[r][c], lSeg[r][c] // 2) - 1, 0)
            res += max(min(dSeg[r][c] // 2, rSeg[r][c]) - 1, 0)
            res += max(min(dSeg[r][c], rSeg[r][c] // 2) - 1, 0)
    return res

if __name__ == "__main__":
    T = int(input())
    for t in range(T):
        R, C = map(int, input().split())
        MAP = [[int(x) for x in input().split()] for _ in range(R)]
        print(f"Case #{t+1}: {solve(R, C, MAP)}")
