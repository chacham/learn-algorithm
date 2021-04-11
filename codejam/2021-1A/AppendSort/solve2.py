import math

def makeNum(n1, n2):
    if n1 < n2:
        return n2, 0
    s1, s2 = str(n1), str(n2)
    ss1 = s1[:len(s2)]
    d = len(s1) - len(s2)
    if ss1 < s2:
        return n2 * (10 ** d), d
    if ss1 > s2:
        return n2 * (10 ** (d+1)), d+1

    res = math.inf
    cnt = math.inf
    for i in range(0, 10):
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
