from functools import reduce

def solve(S):
    def d(start, end):
        nums = S[start:end]
        diffs = []
        for i in range(start+1, end):
            diffs.append(S[i-1] - S[i])
        if all(map(lambda x: x==0, diffs)):
            return 1
        if all(map(lambda x: x == 1, diffs)) or all(map(lambda x: x == -1, diffs)):
            return 2
        if reduce((lambda x, y: x == y), nums[::2]) and reduce((lambda x, y: x == y), nums[1::2]):
            return 4
        if reduce((lambda x, y: x == y), diffs):
            return 5
        return 10

    dp = [0, 0, d(0, 3), d(0, 4), d(0, 5)]
    for i in range(5, len(S)):
        res = 1234567890
        for j in range(max(2, i-5), i-2):
            res = min(res, dp[j] + d(j+1, i+1))
        dp.append(res)
    return dp[-1]

if __name__ == "__main__":
    C = int(input())
    for c in range(C):
        S = [int(s) for s in list(input())]
        print(solve(S))
