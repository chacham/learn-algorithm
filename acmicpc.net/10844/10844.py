if __name__ == "__main__":
    N = int(input())
    
    stairNum = []
    for i in range(N):
        stairNum.append([1] * 10)
    
    for i in range(1, N):
        for j in range(10):
            if j == 0:
                stairNum[i][j] = stairNum[i-1][j+1] % 1000000000
            elif j == 9:
                stairNum[i][j] = stairNum[i-1][j-1] % 1000000000
            else:
                stairNum[i][j] = (stairNum[i-1][j-1] + stairNum[i-1][j+1]) % 1000000000
    
    print(sum([stairNum[N-1][x] for x in range(1, 10)]) % 1000000000)
