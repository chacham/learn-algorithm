if __name__ == "__main__":
    C = int(input())
    for c in range(C):
        N, L = map(int, input().split())
        costs = [int(x) for x in input().split()]

        result = 1000
        for i in range(0, N - L + 1):
            total = sum(costs[i:i+L])
            count = L
            result = min(result, total / count)
            for j in range(i + L, N):
                total += costs[j]
                count += 1
                result = min(result, total / count)
        
        print(result)
