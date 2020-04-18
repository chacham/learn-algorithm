class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        from collections import deque
        res = []
        end = len(graph) - 1
        paths = deque([[0]])
        while paths:
            path = paths.popleft()
            now = path[-1]
            if now == end:
                res.append(path)
                continue
            else:
                for nxt in graph[now]:
                    paths.append(path + [nxt])
        return res
