def check(box):
    for row in box:
        for item in row:
            if item == 0:
                return False
    return True

if __name__ == "__main__":
    M, N = map(int, input().split())

    box = []
    nextBox = []
    points = set()
    nextPoints = set()
    for i in range(N):
        box.append(list(map(int, input().split())))
        nextBox.append(box[-1][:])
        for j in range(M):
            if box[i][j] == 1:
                points.add((i, j))
    
    res = -1
    while points:
        res += 1
        changed = False
        while points:
            row, col = points.pop()

            nextBox[row][col] = 1
            if col > 0 and box[row][col - 1] == 0:
                nextBox[row][col - 1] = 1
                nextPoints.add((row, col - 1))
            if col <  M - 1 and box[row][col + 1] == 0:
                nextBox[row][col + 1] = 1
                nextPoints.add((row, col + 1))
            if row > 0 and box[row - 1][col] == 0:
                nextBox[row - 1][col] = 1
                nextPoints.add((row - 1, col))
            if row < N - 1 and box[row + 1][col] == 0:
                nextBox[row + 1][col] = 1
                nextPoints.add((row + 1, col))
        box, nextBox = nextBox, box
        points, nextPoints = nextPoints, points
    
    if check(box):
        print(res)
    else:
        print(-1)
