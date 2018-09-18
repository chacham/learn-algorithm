def comb(N, K):
    if N == 1:
        return 1
    if K == 0:
        return comb(N-1, K)
    if K == N:
        return comb(N-1, K-1)
    return comb(N-1, K) + comb(N-1, K-1)

if __name__ == "__main__":
    N, K = map(int, input().split())
    print(comb(N, K))