def solution(n, costs):
    answer = 0

    V = set()
    for v1, v2, cost in costs:
        V.add(v1)
        V.add(v2)
    sortedCosts = sorted(costs, key = lambda x: x[2])

    visited = set()

    visited.add(V.pop())
    while V:
        for i in range(len(sortedCosts)):
            v1, v2, cost = sortedCosts[i]
            if v1 in visited and v2 in visited:
                sortedCosts.pop(i)
                break
            elif v1 in visited or v2 in visited:
                if v1 in V:
                    V.remove(v1)
                if v2 in V:
                    V.remove(v2)
                visited.add(v1)
                visited.add(v2)
                answer += cost
                sortedCosts.pop(i)
                break

    return answer

if __name__ == "__main__":
    n = 4
    costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
    print(solution(n, costs))
