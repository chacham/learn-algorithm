def solution(board, moves):
    stack = []
    result = 0
    for move in moves:
        for row in board:
            if row[move-1]:
                stack.append(row[move-1])
                row[move-1] = 0
                break
            while len(stack) >= 2 and stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()
                result += 2
    return result

print(solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]], [1, 5, 3, 5, 1, 2, 1, 4]))
print(solution([[1]], [0]))
print(solution([[0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 2, 1, 0, 0], [0, 2, 1, 0, 0], [0, 2, 1, 0, 0]], [1, 2, 3, 3, 2, 3, 1]))
