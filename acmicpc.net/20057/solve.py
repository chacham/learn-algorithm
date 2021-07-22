def solve(N, A):
    def moves(N):
        res = []
        for n in range(1, N, 2):
            for _ in range(n):
                res.append('L')
            for _ in range(n):
                res.append('D')
            for _ in range(n+1):
                res.append('R')
            for _ in range(n+1):
                res.append('U')
        for _ in range(N-1):
            res.append('L')
        return res

    MOVE_RC = {
        'L': [0, -1],
        'D': [1, 0],
        'R': [0, 1],
        'U': [-1, 0],
    }
    RATIO = {
        'U': [[-2, 0, 5], [-1, 1, 10], [-1, -1, 10], [0, 1, 7], [0, -1, 7], [0, 2, 2], [0, -2, 2], [1, 1, 1], [1, -1, 1]],
        'D': [[2, 0, 5], [1, 1, 10], [1, -1, 10], [0, 1, 7], [0, -1, 7], [0, 2, 2], [0, -2, 2], [-1, 1, 1], [-1, -1, 1]],
        'L': [[0, -2, 5], [1, -1, 10], [-1, -1, 10], [1, 0, 7], [-1, 0, 7], [2, 0, 2], [-2, 0, 2], [1, 1, 1], [-1, 1, 1]],
        'R': [[0, 2, 5], [1, 1, 10], [-1, 1, 10], [1, 0, 7], [-1, 0, 7], [2, 0, 2], [-2, 0, 2], [1, -1, 1], [-1, -1, 1]],
    }

    def blow(R, C, move):
        sand = A[R][C]
        A[R][C] = 0
        moved = 0
        outOfBoard = 0
        for dr, dc, ratio in RATIO[move]:
            r = R + dr
            c = C + dc
            moving = sand * ratio // 100
            if 0 <= r < N and 0 <= c < N:
                A[r][c] += moving
            else:
                outOfBoard += moving
            moved += moving
        dr, dc = MOVE_RC[move]
        r = R + dr
        c = C + dc
        if 0 <= r < N and 0 <= c < N:
            A[r][c] += (sand - moved)
        else:
            outOfBoard += (sand - moved)
        return outOfBoard

    R = C = N // 2
    totalOutOfBoard = 0
    for move in moves(N):
        r, c = MOVE_RC[move]
        R += r
        C += c
        totalOutOfBoard += blow(R, C, move)
    return totalOutOfBoard

if __name__ == "__main__":
    N = int(input())
    A = [[int(x) for x in input().split()] for _ in range(N)]
    print(solve(N, A))
