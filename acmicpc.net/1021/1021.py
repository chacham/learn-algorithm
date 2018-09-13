if __name__ == "__main__":
    N, M = map(int, input().split())
    A = list(map(lambda x: int(x) - 1, input().split()))
    q = list(range(N))
    
    res = 0
    while A:
        now = A.pop(0)
        left = q[:now]
        right = q[now + 1:]
        res += min(len(left), len(right) + 1)
        q = right + left
        A = list(map(lambda x: (x - now) % len(q) if x < now else x - now - 1, A))
    print(res)
