def solution(n):
    if n < 2 or n % 2:
        return 0
    elif n == 2:
        return 3
    else:
        res = [0] * 5001
        res[2] = 3
        for i in range(4, n+1, 2):
            res[i] += 3 * res[i - 2]
            for j in range(4, i):
                res[i] += 2 * res[i - j]
            res[i] += 2
            res[i] %= 1000000007
        return res[n]
