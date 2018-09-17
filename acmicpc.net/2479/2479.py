def matProduct(m1, m2):
    res = []
    for i in m1:
        res.append([0] * len(m2[0]))
    for row in range(len(m1)):
        for col in range(len(m2[0])):
            for i in range(len(m1[0])):
                res[row][col] += (m1[row][i] * m2[i][col]) % 1000000
            res[row][col] %= 1000000
    return res

memo = [[[1, 1], [1, 0]]]
for i in range(1, 61):
    memo.append(matProduct(memo[-1], memo[-1]))

def fibo(N):
    f = [[1, 0], [0, 1]]
    while N:
        now = -1
        n = 1
        while N >= n:
            n *= 2
            now += 1
        n //= 2
        N -= n
        f = matProduct(f, memo[now])
    return matProduct(f, [[1], [0]])[1][0] % 1000000
        

if __name__ == "__main__":
    N = int(input())
    print(fibo(N))