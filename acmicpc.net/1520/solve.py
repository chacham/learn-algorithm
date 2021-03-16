import sys
sys.setrecursionlimit(3000)

D = [(-1, 0), (1, 0), (0, -1), (0, 1)]
DP = [[-1] * 500 for _ in range(500)]

def solve(M, N, MAP):
    def rec(R, C):
        if DP[R][C] != -1:
            return DP[R][C]
        if R == M-1 and C == N-1:
            return 1
        res = 0
        for rd, cd in D:
            r = R + rd
            c = C + cd
            if r < 0 or r >= M or c < 0 or c >= N:
                continue
            if MAP[r][c] >= MAP[R][C]:
                continue
            res += rec(r, c)
        DP[R][C] = res
        return res
    return rec(0, 0)

if __name__ == "__main__":
    M, N = map(int, input().split())
    MAP = [[int(x) for x in input().split()] for _ in range(M)]
    print(solve(M, N, MAP))
