if __name__ == "__main__":
    import math

    N = int(input())
    P = []
    for i in range(N):
        P.append(int(input()))
    P.sort()

    between = []
    for i in range(N - 1):
        between.append(P[i+1] - P[i])

    gcd = between[0]
    for b in between:
        gcd = math.gcd(gcd, b)
    
    print((P[-1] - P[0]) // gcd - N + 1)
