def solve(N, K, S):
    score = 0
    for i in range((N+1)//2):
        if S[i] != S[-i-1]:
            score += 1
    return abs(K-score)   

if __name__ == "__main__":
    T = int(input())
    for t in range(T):
        N, K = map(int, input().split())
        S = input()
        print(f"Case #{t+1}: {solve(N, K, S)}")
