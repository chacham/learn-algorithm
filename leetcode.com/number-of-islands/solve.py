class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        G = [[int(g) for g in row] for row in grid]
        R = len(G)
        C = len(G[0]) if G else 0
        res = 0
        for r in range(R):
            for c in range(C):
                if G[r][c]:
                    res += 1
                    q = [(r, c)]
                    while q:
                        i, j = q.pop()
                        if i < 0 or j < 0 or i >= R or j >= C:
                            continue
                        if G[i][j]:
                            G[i][j] = 0
                            q.append((i-1, j))
                            q.append((i+1, j))
                            q.append((i, j-1))
                            q.append((i, j+1))
        return res
