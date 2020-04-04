if __name__ == "__main__":
    T = int(input())
    for t in range(T):
        N = int(input())
        M = [[int(m) for m in input().split()] for _ in range(N)]
        
        k = 0
        for n in range(N):
            k += M[n][n]
        
        r = 0
        for row in M:
            r += 1 if len(set(row)) != N else 0
        
        c = 0
        for ci in range(N):
            s = set()
            for ri in range(N):
                s.add(M[ri][ci])
            c += 1 if len(s) != N else 0

        print('Case #{}: {} {} {}'.format(t+1, k, r, c))
