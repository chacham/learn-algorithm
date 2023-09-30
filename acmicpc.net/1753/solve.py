import sys
input = sys.stdin.readline
print = sys.stdout.write

from collections import defaultdict
import heapq
from math import inf

def solve(V, E, K, paths):
    res = [inf for _ in range(V+1)]
    h = [(0, K)]
    while h:
        w, v = heapq.heappop(h)
        if res[v] <= w:
            continue
        res[v] = w
        for nextV in paths[v]:
            nextW = w + paths[v][nextV]
            if res[nextV] > nextW:
                heapq.heappush(h, (nextW, nextV))
    return res[1:]

if __name__ == "__main__":
    V, E = map(int, input().split())
    K = int(input())
    paths = defaultdict(lambda: defaultdict(lambda: inf))
    for _ in range(E):
        u, v, w = map(int, input().split())
        paths[u][v] = min(paths[u][v], w)
    res = solve(V, E, K, paths)
    print(" ".join(["INF" if x == inf else str(x) for x in res]))
    print('\n')
