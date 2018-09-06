def check(BOX):
    for row in BOX:
        for item in row:
            if item == 0:
                return False
    return True

if __name__ == "__main__":
    M, N = map(int, input().split())

    BOX = []
    NEXTBOX = []
    for i in range(N):
        BOX.append(list(map(int, input().split())))
        NEXTBOX.append(BOX[-1][:])
    
    changed = True
    res = 0
    while changed and not check(BOX):
        changed = False
        res += 1
        for row in range(N):
            for col in range(M):
                if BOX[row][col] == 1:
                    NEXTBOX[row][col] = 1
                    if col > 0 and BOX[row][col - 1] == 0:
                        NEXTBOX[row][col - 1] = 1
                        changed = True
                    if col <  M - 1 and BOX[row][col + 1] == 0:
                        NEXTBOX[row][col + 1] = 1
                        changed = True
                    if row > 0 and BOX[row - 1][col] == 0:
                        NEXTBOX[row - 1][col] = 1
                        changed = True
                    if row < N - 1 and BOX[row + 1][col] == 0:
                        NEXTBOX[row + 1][col] = 1
                        changed = True
        BOX, NEXTBOX = NEXTBOX, BOX
    
    if check(BOX):
        print(res)
    else:
        print(-1)
