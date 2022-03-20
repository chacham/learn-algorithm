def solve(A, B):
    def P(N):
        head = N // 10
        tail = N % 10
        if head == 0:
            return tail
        if tail == 0:
            return 0
        return P(head) * tail
    def S(N):
        s = 0
        while N:
            s += N % 10
            N //= 10
        return s

    res = 0
    for N in range(A, B+1):
        if P(N) % S(N) == 0:
            res += 1
    return res

if __name__ == "__main__":
    T = int(input())
    for t in range(T):
        A, B = map(int, input().split())
        print(f"Case #{t+1}: {solve(A, B)}")
