class Solution:
    def exist(self, board: "List[List[str]]", word: "str") -> "bool":
        def helper(route):
            row, col = route[-1]
            if len(word) == len(route) and board[row][col] == word[-1]:
                return True
            if len(word) <= len(route) or board[row][col] != word[len(route)-1]:
                return False
            result = False
            if row > 0 and (row-1, col) not in route:
                result = result or helper([*route, (row-1, col)])
            if row < len(board) - 1 and (row+1, col) not in route:
                result = result or helper([*route, (row+1, col)])
            if col > 0 and (row, col-1) not in route:
                result = result or helper([*route, (row, col-1)])
            if col < len(board[0]) - 1 and (row, col+1) not in route:
                result = result or helper([*route, (row, col+1)])
            return result
        if len(word) == 0:
            return True
        for row in range(len(board)):
            for col in range(len(board[0])):
                if helper([(row, col)]):
                    return True
        return False
