if __name__ == "__main__":
    N = int(input())
    A = sorted(set([int(x) for x in input().split()]))
    if len(A) == 1:
        print(0)
    elif len(A) == 2:
        if (A[1] - A[0]) % 2:
            print(A[1] - A[0])
        else:
            print((A[1] - A[0]) // 2)
    elif len(A) == 3:
        if A[1] - A[0] == A[2] - A[1]:
            print(A[1] - A[0])
        else:
            print(-1)
    else:
        print(-1)
