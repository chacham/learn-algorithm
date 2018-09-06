from collections import deque

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
    queue = deque()
    nextQueue = deque()
    for i in range(N):
        BOX.append(list(map(int, input().split())))
        NEXTBOX.append(BOX[-1][:])
        for j in range(M):
            if BOX[i][j] == 1:
                queue.append((i, j))
    
    res = 0
    while queue:
        res += 1
        changed = False
        while queue:
            row, col = queue.popleft()

            NEXTBOX[row][col] = 1
            if col > 0 and BOX[row][col - 1] == 0:
                NEXTBOX[row][col - 1] = 1
                nextQueue.append((row, col - 1))
            if col <  M - 1 and BOX[row][col + 1] == 0:
                NEXTBOX[row][col + 1] = 1
                nextQueue.append((row, col + 1))
            if row > 0 and BOX[row - 1][col] == 0:
                NEXTBOX[row - 1][col] = 1
                nextQueue.append((row - 1, col))
            if row < N - 1 and BOX[row + 1][col] == 0:
                NEXTBOX[row + 1][col] = 1
                nextQueue.append((row + 1, col))
        BOX, NEXTBOX = NEXTBOX, BOX
        queue, nextQueue = nextQueue, queue
    
    if check(BOX):
        print(res - 1)
    else:
        print(-1)
