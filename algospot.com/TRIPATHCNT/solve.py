if __name__ == "__main__":
    C = int(input())
    for _ in range(C):
        N = int(input())
        TRI = [[int(x) for x in input().split()] for _ in range(N)]
        sumMemo = [[0] * (n+1) for n in range(N)]
        cntMemo = [[0] * (n+1) for n in range(N)]
        sumMemo[0][0] = TRI[0][0]
        cntMemo[0][0] = 1
        
        for n in range(1, N):
            sumMemo[n][0] = sumMemo[n-1][0] + TRI[n][0]
            cntMemo[n][0] = 1
            sumMemo[n][n] = sumMemo[n-1][n-1] + TRI[n][n]
            cntMemo[n][n] = 1
            for i in range(1, n):
                if sumMemo[n-1][i-1] > sumMemo[n-1][i]:
                    sumMemo[n][i] = sumMemo[n-1][i-1] + TRI[n][i]
                    cntMemo[n][i] = cntMemo[n-1][i-1]
                elif sumMemo[n-1][i-1] < sumMemo[n-1][i]:
                    sumMemo[n][i] = sumMemo[n-1][i] + TRI[n][i]
                    cntMemo[n][i] = cntMemo[n-1][i]
                else: # Same
                    sumMemo[n][i] = sumMemo[n-1][i-1] + TRI[n][i]
                    cntMemo[n][i] = cntMemo[n-1][i-1] + cntMemo[n-1][i]

        maxSum = max(sumMemo[-1])
        res = 0
        for i in range(N):
            if sumMemo[-1][i] == maxSum:
                res += cntMemo[-1][i]
        print(res)
