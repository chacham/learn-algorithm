import sys
sys.setrecursionlimit(20000)

def solve(FENCES):
    def makeTree(start, end):
        if start == end:
            return None
        minVal = 1234567890
        minValIdx = -1
        for i in range(start, end):
            if minVal > FENCES[i]:
                minVal = FENCES[i]
                minValIdx = i
        return minValIdx, makeTree(start, minValIdx), makeTree(minValIdx+1, end)

    def rec(tree):
        if tree is None:
            return 0, 0
        index, lChild, rChild = tree

        lMax, lLen = rec(lChild)
        rMax, rLen = rec(rChild)

        curLen = lLen + rLen + 1
        curMax = max(FENCES[index] * curLen, lMax, rMax)
        return curMax, curLen

    return rec(makeTree(0, len(FENCES)))[0]

if __name__ == "__main__":
    C = int(input())
    for _ in range(C):
        N = int(input())
        FENCES = [int(x) for x in input().split()]
        print(solve(FENCES))
