def solve(N, L, P):
    from collections import deque
    from math import gcd
    devisor = 1
    for i in range(L - 1):
        devisor = gcd(P[i], P[i+1])
        if devisor != 1 and devisor != P[i]:
            break
    
    result = deque([devisor])
    leftDevisor = devisor
    for j in reversed(range(i+1)):
        leftDevisor = P[j] // leftDevisor
        result.appendleft(leftDevisor)
    for j in range(i+1, L):
        devisor = P[j] // devisor
        result.append(devisor)

    primeToABC = {n: chr(ord('A') + i) for i, n in enumerate(sorted(set(result)))}
    return "".join([primeToABC[n] for n in result])

if __name__ == "__main__":
    T = int(input())
    for t in range(T):
        N, L = map(int, input().split())
        P = [int(n) for n in input().split()]

        print('Case #{}: {}'.format(t+1, solve(N, L, P)))
