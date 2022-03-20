def solve(N, S):
    from collections import deque

    def check5s(S):
        return (S[0] == S[4] and S[1] == S[3]) or (S[1] == S[5] and S[2] == S[4])
    def checkTotal(S):
        return S[0] == S[-1] and S[1] == S[-2] and S[2] == S[-3]
    def check(S):
        if len(S) == 5:
            return checkTotal(S)
        return checkTotal(S) or check5s(S)

    if N < 5:
        return True

    seeds = [S[:6]]
    q = deque([])
    while seeds:
        seed = seeds.pop()
        for i in range(len(seed)):
            if seed[i] == '?':
                seeds.append(seed[:i] + '0' + seed[i+1:])
                seeds.append(seed[:i] + '1' + seed[i+1:])
                break
        else: # if no '?'
            q.append([len(seed), seed])

    while q:
        n, s = q.popleft()
        if check(s):
            continue
        if n == N:
            return True
        nxt = ['0', '1'] if S[n] == '?' else [S[n]]
        for nextc in nxt:
            q.append([n+1, s[1:] + nextc])

    return False

if __name__ == "__main__":
    T = int(input())
    for t in range(T):
        N = int(input())
        S = input()
        print(f"Case #{t+1}: {'POSSIBLE' if solve(N, S) else 'IMPOSSIBLE'}")
