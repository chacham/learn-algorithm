if __name__ == "__main__":
    C = int(input())
    for c in range(C):
        N, M = map(int, input().split())
        A = [int(x) for x in input().split()]
        B = [int(x) for x in input().split()]

        dpA = [[[A[0]]]]
        for i in range(1, N):
            res = []
            for j in range(i):
                if A[j] < A[i]:
                    for lst in dpA[j]:
                        res.append(lst + [A[i]])
            dpA.append(res)

        dpB = [[[B[0]]]]
        for i in range(1, M):
            res = []
            for j in range(i):
                if B[j] < B[i]:
                    for lst in dpB[j]:
                        res.append(lst + [B[i]])
            dpB.append(res)

        res = -1

        for n in range(N):
            for m in range(M):
                for a in dpA[n]:
                    for b in dpB[m]:
                        res = max(res, len(set(a) | set(b)))

        print(res)
