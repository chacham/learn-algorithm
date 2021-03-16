MOD = 10000000
DP = [[-1] * 101 for _ in range(101)]

def solve(N):
    def rec(count, side):
        if DP[count][side] != -1:
            return DP[count][side]
        if count == side:
            return 1

        res = 0
        restCount = count - side
        for nextSide in range(1, restCount + 1):
            res += rec(restCount, nextSide) * (side + nextSide - 1)
        DP[count][side] = res % MOD
        return DP[count][side]

    res = 0
    for side in range(1, N+1):
        res += rec(N, side)
    return res % MOD

if __name__ == "__main__":
    C = int(input())

    for _ in range(C):
        N = int(input())
        print(solve(N))
