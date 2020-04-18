class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        end = len(graph) - 1
        path = [0]

        def dfs():
            now = path[-1]
            if now == end:
                res.append(path.copy())
                return
            for node in graph[now]:
                path.append(node)
                dfs()
                path.pop()

        dfs()
        return res
