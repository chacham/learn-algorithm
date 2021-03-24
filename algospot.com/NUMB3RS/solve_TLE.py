def square(sqmat, SIZE):
    res = [[0] * SIZE for _ in range(SIZE)]
    for r in range(SIZE):
        for c in range(SIZE):
            for i in range(SIZE):
                res[r][c] += sqmat[r][i] * sqmat[i][c]
    return res

def multi(vec, sqmat, SIZE):
    res = [0] * SIZE
    for c in range(SIZE):
        for i in range(SIZE):
            res[c] += vec[i] * sqmat[i][c]
    return res

def solve(N, D, P, A, T, Q):
    sumA = [sum(row) for row in A]
    trans = [[v / sumA[i] for v in row] for i, row in enumerate(A)]

    p = [0] * N
    p[P] = 1

    while D:
        if D % 2:
            p = multi(p, trans, N)
        trans = square(trans, N)
        D >>= 1
    
    res = []
    for q in Q:
        res.append(p[q])
    return res

if __name__ == "__main__":
    C = int(input())
    for _ in range(C):
        N, D, P = map(int, input().split())
        A = [[int(x) for x in input().split()] for _ in range(N)]
        T = int(input())
        Q = [int(x) for x in input().split()]
        print(*solve(N, D, P, A, T, Q))
