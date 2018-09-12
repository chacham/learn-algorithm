from collections import deque

if __name__ == "__main__":
    N, M = map(int, input().split())
    
    res = []
    q = deque(range(1, N+1))
    while q:
        for i in range(M):
            q.append(q.popleft())
        res.append(q.pop())

    print('<', end='')
    print(*res, sep=', ', end='')
    print('>')