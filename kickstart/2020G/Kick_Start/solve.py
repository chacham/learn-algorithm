def solve(S: str):
    ends = [0] * len(S)
    for i in reversed(range(len(S) - 4)):
        ends[i] = ends[i+1]
        if S.startswith("START", i):
            ends[i] = ends[i] + 1
    
    res = 0
    for i in range(len(S) - 8):
        if S.startswith("KICK", i):
            res += ends[i+4]
    return res

if __name__ == "__main__":
    T = int(input())
    for t in range(T):
        S = input()
        print(f"Case #{t+1}: {solve(S)}")
