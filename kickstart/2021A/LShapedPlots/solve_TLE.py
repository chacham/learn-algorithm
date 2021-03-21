def solve(R, C, MAP):
    hSeg = [[0] * C for _ in range(R)]
    vSeg = [[0] * C for _ in range(R)]

    hSeg[0][0] = MAP[0][0]
    vSeg[0][0] = MAP[0][0]
    for c in range(1, C):
        hSeg[0][c] = hSeg[0][c-1] + 1 if MAP[0][c] else 0
        vSeg[0][c] = MAP[0][c]
    for r in range(1, R):
        hSeg[r][0] = MAP[r][0]
        vSeg[r][0] = vSeg[r-1][0] + 1 if MAP[r][0] else 0
    
    for r in range(1, R):
        for c in range(1, C):
            hSeg[r][c] = hSeg[r][c-1] + 1 if MAP[r][c] else 0
            vSeg[r][c] = vSeg[r-1][c] + 1 if MAP[r][c] else 0

    res = 0
    for r in range(0, R):
        for c in range(0, C):
            for size in range(2, hSeg[r][c] + 1):
                if r+size*2-1 < R and vSeg[r+size*2-1][c] >= size*2:
                    res += 1
                if vSeg[r][c-size+1] >= size * 2:
                    res += 1
                if r+size*2-1 < R and vSeg[r+size*2-1][c-size+1] >= size * 2:
                    res += 1
                if vSeg[r][c] >= size * 2:
                    res += 1
            for size in range(2, vSeg[r][c] + 1):
                if c+size*2-1 < C and hSeg[r][c+size*2-1] >= size*2:
                    res += 1
                if hSeg[r-size+1][c] >= size * 2:
                    res += 1
                if c+size*2-1 < C and hSeg[r-size+1][c+size*2-1] >= size*2:
                    res += 1
                if hSeg[r][c] >= size * 2:
                    res += 1
            
    return res

if __name__ == "__main__":
    T = int(input())
    for t in range(T):
        R, C = map(int, input().split())
        MAP = [[int(x) for x in input().split()] for _ in range(R)]
        print(f"Case #{t+1}: {solve(R, C, MAP)}")
