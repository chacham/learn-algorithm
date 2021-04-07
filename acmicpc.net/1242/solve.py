def solve(N, K, M):
    remove = -1
    res = 0
    M -= 1
    while M >= 0:
        res += 1
        remove = (remove + K) % N
        if remove == M:
            return res
        if remove < M:
            M -= 1
        N -= 1
        remove -= 1

if __name__ == "__main__":
    N, K, M = map(int, input().split())
    print(solve(N, K, M))
