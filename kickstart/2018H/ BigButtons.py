if __name__ == "__main__":
    T = int(input())

    for t in range(T):
        N, P = map(int, input().split())
        p = []
        for _ in range(P):
            p.append(input())
        p.sort(key=lambda x: len(x))

        filtered = []
        for s in p:
            if all(map(lambda x: not s.startswith(x), filtered)):
                filtered.append(s)

        res = 1 << N
        for s in filtered:
            res -= 1 << (N - len(s))

        print("Case #{}: {}".format(t+1, res))
