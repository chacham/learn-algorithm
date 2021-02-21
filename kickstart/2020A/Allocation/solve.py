if __name__ == "__main__":
    T = int(input())
    for t in range(1, T+1):
        N, B = map(int, input().split())
        A = [int(a) for a in input().split()]
        sA = sorted(A)

        i = 0
        while i < N and sA[i] <= B:
            B -= sA[i]
            i += 1

        print("Case #{}: {}".format(t, i))
