def solve(N, L):
    res = 0
    for i in range(N - 1):
        minIdx = i
        minVal = L[i]
        for j in range(i, N):
            if L[j] < minVal:
                minIdx = j
                minVal = L[j]
        res += minIdx - i + 1
        # print(f"{i}, {minIdx},{minVal}, {res}")
        # print(f" {L}")
        for j in range((minIdx - i + 1) // 2):
            L[i+j], L[minIdx-j] = L[minIdx-j], L[i+j]
        # print(f" {L}")
    return res

if __name__ == "__main__":
    T = int(input())
    for t in range(T):
        N = int(input())
        L = [int(l) for l in input().split()]
        print(f"Case #{t+1}: {solve(N, L)}")
