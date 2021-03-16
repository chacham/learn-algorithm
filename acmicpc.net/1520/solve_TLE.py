D = [(-1, 0), (1, 0), (0, -1), (0, 1)]

if __name__ == "__main__":
    M, N = map(int, input().split())
    MAP = [[int(x) for x in input().split()] for _ in range(M)]
    stack = [(0, 0)]
    res = 0
    while stack:
        R, C = stack.pop()
        if R == M-1 and C == N-1:
            res += 1
            continue
        for rd, cd in D:
            r = R + rd
            c = C + cd
            if r < 0 or r >= M or c < 0 or c >= N:
                continue
            if MAP[r][c] >= MAP[R][C]:
                continue
            stack.append((r, c))
    print(res)
    