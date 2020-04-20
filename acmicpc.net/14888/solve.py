if __name__ == "__main__":
    from collections import deque

    N = int(input())
    As = deque([int(a) for a in input().split()])
    plus, minus, prod, div = map(int, input().split())

    def dfs(acc, plus, minus, prod, div, res_max, res_min):
        if not As:
            return max(acc, res_max), min(acc, res_min)

        a = As.popleft()
        if plus:
            max_tmp, min_tmp = dfs(acc + a, plus - 1, minus, prod, div, res_max, res_min)
            res_max = max(max_tmp, res_max)
            res_min = min(min_tmp, res_min)
        if minus:
            max_tmp, min_tmp = dfs(acc - a, plus, minus - 1, prod, div, res_max, res_min)
            res_max = max(max_tmp, res_max)
            res_min = min(min_tmp, res_min)
        if prod:
            max_tmp, min_tmp = dfs(acc * a, plus, minus, prod - 1, div, res_max, res_min)
            res_max = max(max_tmp, res_max)
            res_min = min(min_tmp, res_min)
        if div:
            if acc >= 0:
                max_tmp, min_tmp = dfs(acc // a, plus, minus, prod, div - 1, res_max, res_min)
                res_max = max(max_tmp, res_max)
                res_min = min(min_tmp, res_min)
            else:
                max_tmp, min_tmp = dfs(-(-acc // a), plus, minus, prod, div - 1, res_max, res_min)
                res_max = max(max_tmp, res_max)
                res_min = min(min_tmp, res_min)
        As.appendleft(a)

        return res_max, res_min

    res_max, res_min = dfs(As.popleft(), plus, minus, prod, div, -1234567890, 1234567890)
    print(res_max)
    print(res_min)
