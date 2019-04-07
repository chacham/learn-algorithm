def solve(N, L, P):
    import math
    devisor = P[0] // math.gcd(P[0], P[1])
    result = [devisor]
    for p in P:
        devisor = p // devisor
        result.append(devisor)
    
    abcMap = {n: chr(ord('A') + i) for i, n in enumerate(sorted(set(result)))}
    return "".join([abcMap[n] for n in result])

if __name__ == "__main__":
    T = int(input())
    for t in range(T):
        N, L = map(int, input().split())
        P = [int(n) for n in filter(lambda x: x, input().strip().split())]
        
        print('Case #{}: {}'.format(t+1, solve(N, L, P)))
