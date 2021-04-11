import math

def makeNum(n1, n2):
    if n1 < n2:
        return n2, 0
    res = math.inf
    cnt = math.inf
    for i in range(10):
        tmpRes, tmpCnt = makeNum(n1, n2 * 10 + i)
        if tmpCnt < cnt:
            res = tmpRes
            cnt = tmpCnt
    return res, cnt + 1
    
def solve(N, X):
    res = 0
    for i in range(1, N):
        nextX, cnt = makeNum(X[i-1], X[i])
        X[i] = nextX
        res += cnt
    return res

if __name__ == "__main__":
    T = int(input())
    for t in range(T):
        N = int(input())
        X = [int(x) for x in input().split()]

        print(f"Case #{t+1}: {solve(N, X)}")
