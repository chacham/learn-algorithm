def solve(S):
    sumS = sum([int(c) for c in S])
    d = (9 - (sumS % 9)) % 9
    if d == 0:
        return S[:1] + '0' + S[1:]
    for i in range(len(S)):
        if int(S[i]) > d:
            return S[:i] + str(d) + S[i:]
    return S + str(d)

if __name__ == "__main__":
    T = int(input())
    for t in range(T):
        S = input()
        print(f"Case #{t+1}: {solve(S)}")
