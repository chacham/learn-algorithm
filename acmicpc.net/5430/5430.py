from collections import deque

def solve(P, X):
    straight = True
    for p in P:
        if p == 'R':
            straight = not straight
        elif straight:
            X.popleft()
        else:
            X.pop()
    return X if straight else reversed(X)

if __name__ == "__main__":
    T = int(input())
    for t in range(T):
        try:
            P = input()
            N = int(input())
            X = input()
            X = deque(int(x) for x in X[1:-1].split(',')) if N > 0 else deque()

            res = solve(P, X)
            print('[', end='')
            print(*res, sep=',', end='')
            print(']')

        except:
            print("error")