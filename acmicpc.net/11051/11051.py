comb = {(1, 0): 1, (1, 1): 1}
for n in range(2, 1001):
    comb[(n, 0)] = comb[(n-1, 0)]
    for k in range(1, n):
        comb[(n, k)] = (comb[(n-1, k-1)] + comb[(n-1, k)]) % 10007
    comb[(n, n)] = comb[(n-1, n-1)]

if __name__ == "__main__":
    N, K = map(int, input().split())
    print(comb[(N, K)])