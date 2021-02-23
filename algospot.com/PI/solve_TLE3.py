import sys
sys.setrecursionlimit(100000)

def solve(S):
    def d(start, end):
        c1, c2, c3, c4 = True, True, True, True
        for i in range(start+1, end):
            if S[i] != S[i-1]:
                c1 = False
            if i > start+1:
                if S[i-2] - S[i-1] != S[i-1] - S[i]:
                    c2 = False
                    c4 = False
                if S[i-1] - S[i] != 1 and S[i-1] - S[i] != -1:
                    c2 = False
                if S[i-2] != S[i]:
                    c3 = False
        if c1:
            return 1
        if c2:
            return 2
        if c3:
            return 4
        if c4:
            return 5
        return 10

    dp = {0: 0, 1: 0, 2: d(0, 3), 3: d(0, 4), 4: d(0, 5)}
    def rec(i):
        if i in dp:
            return dp[i]
        res = 1234567890
        for j in range(max(2, i-5), i-2):
            res = min(res, rec(j) + d(j+1, i+1))
        dp[i] = res
        return res

    return rec(len(S)-1)

if __name__ == "__main__":
    C = int(input())
    for c in range(C):
        S = [int(s) for s in list(input())]
        print(solve(S))
