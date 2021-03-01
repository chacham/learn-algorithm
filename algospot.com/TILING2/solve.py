if __name__ == "__main__":
    MOD = 1000000007
    res = [1, 2]
    for i in range(2, 100):
        res.append((res[-1] + res[-2]) % MOD)
    C = int(input())
    for c in range(C):
        N = int(input())
        print(res[N-1])
