def swaped(s, a, b):
    return s[:a] + s[b] + s[a+1:b] + s[a] + s[b+1:]

if __name__ == "__main__":
    T = int(input())
    for t in range(1, T+1):
        NUM, ITER = input().split()
        ITER = int(ITER)
        POS = [(i, j) for i in range(len(NUM)) for j in range(len(NUM)) if i < j]

        now = set()
        now.add(NUM)
        after = set()
        for i in range(ITER):
            while now:
                s = now.pop()
                for i, j in POS:
                    after.add(swaped(s, i, j))
            now, after = after, now
        print("#", t, ' ', max(map(int, now)), sep='')
