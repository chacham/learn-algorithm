from collections import deque

if __name__ == "__main__":
    N = int(input())
    MAP = [[int(n) for n in input().split()] for _ in range(N)]

    time = 0
    sSize = 2
    sAte = 0
    sRow, sCol = 0, 0
    for i in range(N):
        for j in range(N):
            if MAP[i][j] == 9:
                sRow, sCol = i, j
                MAP[i][j] = 0
    
    while True:
        queue = deque()
        queue.append((sRow, sCol, 0))
        visited = set()
        ate = 0
        ateDist = 123456789

        while queue:
            row, col, dist = queue.popleft()
            if (row, col) in visited or dist > ateDist or row < 0 or col < 0 or row >= N or col >= N:
                continue

            visited.add((row, col))
            if MAP[row][col] == 0 or MAP[row][col] == sSize:
                queue.append((row - 1, col, dist + 1))
                queue.append((row + 1, col, dist + 1))
                queue.append((row, col - 1, dist + 1))
                queue.append((row, col + 1, dist + 1))
            elif MAP[row][col] < sSize:
                if ateDist > dist:
                    ate = (row, col)
                    ateDist = dist
                elif row < ate[0] or (row == ate[0] and col < ate[1]):
                    ate = (row, col)

        if ate == 0:
            break
        
        MAP[ate[0]][ate[1]] = 0
        sRow, sCol = ate
        sAte += 1
        if sAte == sSize:
            sAte = 0
            sSize += 1
        time += ateDist
        
    print(time)





