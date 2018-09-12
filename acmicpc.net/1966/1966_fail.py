if __name__ == "__main__":
    T = int(input())
    for t in range(T):
        N, M = map(int, input().split())
        P = list(map(int, input().split()))

        biggerMin = float('inf')
        biggers = 0
        samesAfterBiggerMin = 0
        for i in range(M+1, N):
            if P[M] == P[i]:
                samesAfterBiggerMin += 1
            if P[M] < P[i]:
                biggers += 1
                if biggerMin >= P[i]:
                    biggerMin = P[i]
                    samesAfterBiggerMin = 0
        if biggers == 0:
            samesAfterBiggerMin = 0
        for i in range(0, M):
            if P[M] == P[i]:
                samesAfterBiggerMin += 1
            if P[M] < P[i]:
                biggers += 1
                if biggerMin >= P[i]:
                    biggerMin = P[i]
                    samesAfterBiggerMin = 0
        print(biggers + samesAfterBiggerMin + 1)

