if __name__ == "__main__":
    T = int(input())
    for t in range(T):
        N = int(input())
        SE = []
        for n in range(N):
            s, e = map(int, input().split())
            SE.append((s, e, n))

        C = 0
        J = 0
        res = []
        SSE = sorted(SE)
        for i, (s, e, n) in enumerate(SSE):
            if C <= s:
                C = e
                res.append((n, 'C'))
            elif J <= s:
                J = e
                res.append((n, 'J'))
            else:
                res = [(0, 'IMPOSSIBLE')]
        
        res = [v for (n, v) in sorted(res)]

        print('Case #{}: {}'.format(t+1, ''.join(res)))
