def solve(N, P, S):
    S.sort()

    result = sum([S[P-1] - n for n in S[:P]])
    last = result
    # print(N, P, S, len(S) - P + 1)
    for i in range(1, len(S) - P + 1): # i for first
        # print(i, last, S[i+P-2], S[i-1], S[i+P-1])
        last = last - (S[i+P-2] - S[i-1])
        last += (P-1) * (S[i+P-1] - S[i+P-2])
        result = min(result, last)
    return result

if __name__ == "__main__":
    T = int(input())
    for t in range(T):
        N, P = map(int, input().split())
        S = [int(n) for n in input().split()]
        print("Case #{}: {}".format(t+1, solve(N, P, S)))
