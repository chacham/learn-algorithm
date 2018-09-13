if __name__ == "__main__":
    N = int(input())
    
    ascNum = []
    ascNum.append([1] * 10)
    ascNum.append([1] * 10)
    
    for i in range(1, N):
        for j in range(10):
            if j == 0:
                ascNum[1][j] = ascNum[0][j]
            else:
                ascNum[1][j] = (ascNum[1][j-1] + ascNum[0][j]) % 10007
        ascNum[0], ascNum[1] = ascNum[1], ascNum[0]
    
    print(sum([ascNum[0][x] for x in range(10)]) % 10007)
