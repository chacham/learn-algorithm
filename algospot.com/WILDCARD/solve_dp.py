def check(p, s):
    dp = {}

    def rec(i, j):
        if (i, j) in dp:
            return dp[(i, j)]
        if i == len(p):
            if j == len(s):
                return True
            return False
        if p[i] == '*':
            if j < len(s):
                res = rec(i, j+1) or rec(i+1, j)
                dp[(i, j)] = res
                return res
            res = rec(i+1, j)
            return res
        if j == len(s):
            return False
        if p[i] == '?' and j < len(s):
            res = rec(i+1, j+1)
            dp[(i, j)] = res
            return res
        if p[i] == s[j]:
            res = rec(i+1, j+1)
            dp[(i, j)] = res
            return res
        return False
    return rec(0, 0)


if __name__ == "__main__":
    C = int(input())
    for c in range(C):
        W = input()
        N = int(input())
        FILES = [input() for n in range(N)]

        res = []
        for file in FILES:
            if check(W, file):
                res.append(file)

        for file in sorted(res):
            print(file)
