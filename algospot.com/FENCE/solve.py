import sys
import random
sys.setrecursionlimit(20000)

def solve(FENCES):
    def makeTree():
        heightList = sorted([(i, h) for i, h in enumerate(
            FENCES)], key=lambda x: (x[1], random.random()))
        root = [heightList[0][0], None, None]
        for index in range(1, len(heightList)):
            i, _ = heightList[index]
            parent = root
            while True:
                if i < parent[0]:
                    if parent[1] is None:
                        parent[1] = [i, None, None]
                        break
                    else:
                        parent = parent[1]
                        continue
                else:
                    if parent[2] is None:
                        parent[2] = [i, None, None]
                        break
                    else:
                        parent = parent[2]
                        continue
        return root

    def rec(tree):
        if tree is None:
            return 0, 0
        index, lChild, rChild = tree

        lMax, lLen = rec(lChild)
        rMax, rLen = rec(rChild)

        curLen = lLen + rLen + 1
        curMax = max(FENCES[index] * curLen, lMax, rMax)
        return curMax, curLen

    return rec(makeTree())[0]


if __name__ == "__main__":
    C = int(input())
    for _ in range(C):
        N = int(input())
        FENCES = [int(x) for x in input().split()]
        print(solve(FENCES))
