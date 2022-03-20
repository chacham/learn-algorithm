def solve(I, P):
    ii = 0
    pi = 0
    res = 0
    while ii < len(I) and pi < len(P):
        while pi < len(P) and I[ii] != P[pi]:
            pi += 1
            res += 1
        ii += 1
        pi += 1
    if ii == len(I) and pi <= len(P):
        return res + (len(P) - pi)
    else:
        return -1

if __name__ == "__main__":
    T = int(input())
    for t in range(T):
        I = input()
        P = input()
        res = solve(I, P)
        print(f"Case #{t+1}: {res if res >= 0 else 'IMPOSSIBLE'}")
