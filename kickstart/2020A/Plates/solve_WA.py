if __name__ == "__main__":
    T = int(input())
    for t in range(1, T+1):
        N, K, P = map(int, input().split())
        S = [[int(x) for x in input().split()] for _ in range(N)]

        nbr = []
        for si, s in enumerate(S):
            sumS = 0
            for k in range(K):
                sumS += s[k]
                nbr.append((si, k+1, sumS/(k+1)))
        nbr.sort(key=lambda x: x[2])

        res = 0
        visited = [0] * N
        restP = P
        while restP:
            si, end, _ = nbr.pop()
            if visited[si] < end and restP >= (end - visited[si]):
                restP -= (end - visited[si])
                for i in range(visited[si], end):
                    res += S[si][i]
                    print(S[si][i])
                visited[si] = end

        print("Case #{}: {}".format(t, res))
