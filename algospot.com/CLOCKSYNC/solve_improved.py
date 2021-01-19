SWITCH = [
    [8, [6, 7, 8, 10, 12]],
    [11, [3, 7, 9, 11]],
    [13, [3, 4, 5, 9, 13]],
    [6, [0, 4, 5, 6, 7]],
    [10, [4, 10, 14, 15]],
    [7, [4, 5, 7, 14, 15]],
    [4, [1, 2, 3, 4, 5]],
    [3, [3, 14, 15]],
    [14, [0, 2, 14, 15]],
    [1, [0, 1, 2]],
]

if __name__ == "__main__":
    C = int(input())
    for _ in range(C):
        CLOCKS = [(int(x) // 3) % 4 for x in input().split()]

        res = 0
        for s, connections in SWITCH:
            if CLOCKS[s]:
                d = 4 - CLOCKS[s]
                for conn in connections:
                    CLOCKS[conn] = (CLOCKS[conn] + d) % 4
                res += d

        if not any(CLOCKS):
            print(res)
        else:
            print(-1)
