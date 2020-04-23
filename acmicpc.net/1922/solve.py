import sys
import heapq
input = sys.stdin.readline

def solve(N, M, path):
    parent = [0 for _ in range(N + 1)]
    def merge(a, b):
        rootA = a
        rootB = b
        while parent[rootA]:
            rootA = parent[rootA]
        while parent[rootB]:
            rootB = parent[rootB]
        if rootA == rootB:
            return False
        parent[rootA] = rootB
        return True

    heapq.heapify(path)

    res = 0
    while path:
        c, a, b = heapq.heappop(path)
        if a == b or not merge(a, b): # Same node or already merged
            continue
        res += c
    return res

if __name__ == "__main__":
    N = int(input())
    M = int(input())

    path = []
    for m in range(M):
        a, b, c = map(int, input().split())
        path.append((c, a, b))

    print(solve(N, M, path))
    
