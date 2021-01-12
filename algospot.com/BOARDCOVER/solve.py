if __name__ == "__main__":
    C = int(input())
    for c in range(C):
        H, W = map(int, input().split())
        BOARD = [[b == '.' for b in input()]
                 for _ in range(H)]  # True for white

        def findTopLeft(BOARD, curRow, curCol):
            for c in range(curCol, W):
                if BOARD[curRow][c]:
                    return curRow, c
            for r in range(curRow + 1, H):
                for c in range(W):
                    if BOARD[r][c]:
                        return r, c
            return None

        def dfs(BOARD, curRow, curCol):
            emptyTopLeft = findTopLeft(BOARD, curRow, curCol)
            if not emptyTopLeft:
                return 1
            r, c = emptyTopLeft

            result = 0
            # UL
            if r+1 < H and c+1 < W and BOARD[r][c] and BOARD[r][c+1] and BOARD[r+1][c+1]:
                BOARD[r][c] = False
                BOARD[r][c+1] = False
                BOARD[r+1][c+1] = False
                result += dfs(BOARD, r, c + 2)
                BOARD[r][c] = True
                BOARD[r][c+1] = True
                BOARD[r+1][c+1] = True
            # UR
            if r+1 < H and c+1 < W and BOARD[r][c] and BOARD[r][c+1] and BOARD[r+1][c]:
                BOARD[r][c] = False
                BOARD[r][c+1] = False
                BOARD[r+1][c] = False
                result += dfs(BOARD, r, c + 2)
                BOARD[r][c] = True
                BOARD[r][c+1] = True
                BOARD[r+1][c] = True
            # DL
            if r+1 < H and c-1 >= 0 and BOARD[r][c] and BOARD[r+1][c] and BOARD[r+1][c-1]:
                BOARD[r][c] = False
                BOARD[r+1][c] = False
                BOARD[r+1][c-1] = False
                result += dfs(BOARD, r, c + 1)
                BOARD[r][c] = True
                BOARD[r+1][c] = True
                BOARD[r+1][c-1] = True
            # DR
            if r+1 < H and c+1 < W and BOARD[r][c] and BOARD[r+1][c] and BOARD[r+1][c+1]:
                BOARD[r][c] = False
                BOARD[r+1][c] = False
                BOARD[r+1][c+1] = False
                result += dfs(BOARD, r, c + 1)
                BOARD[r][c] = True
                BOARD[r+1][c] = True
                BOARD[r+1][c+1] = True

            return result

        print(dfs(BOARD, 0, 0))
