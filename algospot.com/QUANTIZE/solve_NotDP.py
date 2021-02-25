def solve(N, S, A):
    def mse(arr):
        mean = round(sum(arr)/len(arr))
        return sum(map(lambda x: (x-mean)**2, arr))

    def rec(s, a):
        if a == 0:
            return 0
        if s == 0:
            return 1234567890
        if s == 1:
            return mse(A[:a])
        res = 1234567890
        for i in range(a):
            res = min(res, rec(s-1, i) + mse(A[i:a]))
        return res

    return rec(S, len(A))

if __name__ == "__main__":
    C = int(input())
    for c in range(C):
        N, S = map(int, input().split())
        A = sorted([int(a) for a in input().split()])
        print(solve(N, S, A))
