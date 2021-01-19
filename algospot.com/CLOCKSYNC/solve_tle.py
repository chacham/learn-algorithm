SWITCH = [
    [0, 1, 2],
    [3, 7, 9, 11],
    [4, 10, 14, 15],
    [0, 4, 5, 6, 7],
    [6, 7, 8, 10, 12],
    [0, 2, 14, 15],
    [3, 14, 15],
    [4, 5, 7, 14, 15],
    [1, 2, 3, 4, 5],
    [3, 4, 5, 9, 13]
]

if __name__ == "__main__":
    C = int(input())
    for _ in range(C):
        CLOCKS = [(int(x) // 3) % 4 for x in input().split()]

        def dfs(curSwitch, curCount, minCount):
            if not any(CLOCKS):
                return curCount
            if curCount >= minCount or curSwitch == 10:
                return minCount
            for i in range(4):
                minCount = min(minCount, dfs(
                    curSwitch + 1, curCount + i, minCount))
                for connected in SWITCH[curSwitch]:
                    CLOCKS[connected] += 1
                    CLOCKS[connected] %= 4
            return minCount

        res = dfs(0, 0, 1234567890)
        if res == 1234567890:
            print(-1)
        else:
            print(res)
