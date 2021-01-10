if __name__ == "__main__":
    C = int(input())
    for c in range(C):
        N, M = map(int, input().split())
        F = [[] for _ in range(N)]
        lst = [int(x) for x in input().split()]
        while lst:
            a = lst.pop()
            b = lst.pop()
            F[a].append(b)
            F[b].append(a)

        def rec(visited):
            if len(visited) == N:
                return 1
            res = 0
            for a in range(N):
                if a not in visited:
                    break
            visited.add(a)
            for b in F[a]:
                if b not in visited:
                    visited.add(b)
                    res += rec(visited)
                    visited.remove(b)
            visited.remove(a)
            return res

        result = rec(set())
        print(result)
