from collections import deque

def solve(X, Y, S):
    COST = {
        'C': {'C': 0, 'J': X},
        'J': {'C': Y, 'J': 0},
    }
    DP = {
        'C': [1234567890] * len(S),
        'J': [1234567890] * len(S),
    }

    q = deque()
    if S[0] == '?':
        q.append(('C', 0, 0))
        q.append(('J', 0, 0))
    else:
        q.append((S[0], 0, 0))
    res = 1234567890
    while q:
        lastChar, lastIdx, lastCost = q.popleft()
        if lastIdx == len(S) - 1:
            res = min(res, lastCost)
            continue
        if lastCost >= DP[lastChar][lastIdx]:
            continue
        DP[lastChar][lastIdx] = lastCost
        curIdx = lastIdx + 1
        curChar = S[curIdx]
        if curChar != '?':
            q.append((curChar, curIdx, lastCost + COST[lastChar][curChar]))
        else:
            q.append(('C', curIdx, lastCost + COST[lastChar]['C']))
            q.append(('J', curIdx, lastCost + COST[lastChar]['J']))
    return res

if __name__ == "__main__":
    T = int(input())
    for t in range(T):
        x, y, S = input().split()
        X, Y = int(x), int(y)
        print(f"Case #{t+1}: {solve(X, Y, S)}")
