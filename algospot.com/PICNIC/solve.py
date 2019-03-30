if __name__ == "__main__":
    def check(n, friends, visited, start):
        if all(visited):
            return 1
        result = 0

        now = 0
        for now in range(start, n):
            if not visited[now]:
                break

        visited[now] = True
        result = 0
        for i in range(now+1, n):
            if i in friends[now] and not visited[i]:
                visited[i] = True
                result += check(n, friends, visited, now)
                visited[i] = False
        visited[now] = False
        return result

    C = int(input())
    for c in range(C):
        n, m = map(int, input().split())
        inputPairs = [int(x) for x in input().split()]
        friends = [[] for _ in range(n)]
        for i in range(m):
            a, b = inputPairs[i*2], inputPairs[i*2+1]
            friends[a].append(b)
            friends[b].append(a)
        for arr in friends:
            arr.sort()

        print(check(n, friends, [False] * n, 0))
