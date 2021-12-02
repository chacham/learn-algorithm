def solve(N, M, K, A, R):
    def rotate(r, c, s):
        for i in range(1, s+1):
            r1, c1 = r-i, c-i
            for j in range(i*2):
                A[r1][c1], A[r1+1][c1] = A[r1+1][c1], A[r1][c1]
                r1 += 1
            for j in range(i*2):
                A[r1][c1], A[r1][c1+1] = A[r1][c1+1], A[r1][c1]
                c1 += 1
            for j in range(i*2):
                A[r1][c1], A[r1-1][c1] = A[r1-1][c1], A[r1][c1]
                r1 -= 1
            for j in range(i*2-1):
                A[r1][c1], A[r1][c1-1] = A[r1][c1-1], A[r1][c1]
                c1 -= 1
    def revert(r, c, s):
        for i in range(1, s+1):
            r1, c1 = r-i, c-i
            for j in range(i*2):
                A[r1][c1], A[r1][c1+1] = A[r1][c1+1], A[r1][c1]
                c1 += 1
            for j in range(i*2):
                A[r1][c1], A[r1+1][c1] = A[r1+1][c1], A[r1][c1]
                r1 += 1
            for j in range(i*2):
                A[r1][c1], A[r1][c1-1] = A[r1][c1-1], A[r1][c1]
                c1 -= 1
            for j in range(i*2-1):
                A[r1][c1], A[r1-1][c1] = A[r1-1][c1], A[r1][c1]
                r1 -= 1
    
    def iter(restR):
        if not restR:
            return min([sum(row) for row in A])
        minSum = 1234567890
        for i, curR in enumerate(restR):
            r, c, s = curR
            rotate(r, c, s)
            minSum = min(minSum, iter(restR[:i] + restR[i+1:]))
            revert(r, c, s)
        return minSum

    return iter(R)
        

if __name__ == "__main__":
    N, M, K = map(int, input().split())
    A = [[int(x) for x in input().split()] for _ in range(N)]
    R = [[int(x) for x in input().split()] for _ in range(K)]
    for rotate in R:
        rotate[0] -= 1
        rotate[1] -= 1
    print(solve(N, M, K, A, R))

