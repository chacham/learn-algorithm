if __name__ == "__main__":
    C = int(input())

    TILE = [1, 1, 2]
    for i in range(100):
        TILE.append(TILE[-1] + TILE[-2])

    for _ in range(C):
        N = int(input())

        if N % 2 == 0:
            print((TILE[N] - TILE[N//2] - TILE[N//2-1]) % 1000000007)
        else:
            print((TILE[N] - TILE[N//2]) % 1000000007) 
