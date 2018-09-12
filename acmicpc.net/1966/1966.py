from collections import deque

if __name__ == "__main__":
    T = int(input())
    for t in range(T):
        N, M = map(int, input().split())
        P = deque(map(int, input().split()))
        sortedP = deque(sorted(P, reverse=True))

        result = 1
        while True:
            if P[0] == sortedP[0]:
                if M == 0:
                    print(result)
                    break
                P.popleft()
                sortedP.popleft()
                result += 1
                M -= 1
            else:
                P.append(P.popleft())
                M -= 1
                if M < 0:
                    M += len(P)
