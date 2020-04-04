if __name__ == "__main__":
    T = int(input())
    for t in range(T):
        S = input()
        res = []

        d = 0
        for s in S:
            n = int(s)
            while d < n:
                res.append('(')
                d += 1
            while d > n:
                res.append(')')
                d -= 1
            res.append(s)
        while d:
            res.append(')')
            d -= 1

        print('Case #{}: {}'.format(t+1, ''.join(res)))
