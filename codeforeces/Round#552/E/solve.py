if __name__ == "__main__":
    import heapq
    N, K = map(int, input().split())
    A = [int(x) for x in input().split()]
    result = [0 for _ in range(N)]
    Aheap = [(-x, i) for i, x in enumerate(A)]
    heapq.heapify(Aheap)

    team = 1
    while Aheap:
        _, index = heapq.heappop(Aheap)
        if result[index]:
            continue
        result[index] = team

        count = 0
        k = 0
        while index - k - 1 >= 0 and count < K:
            if result[index - k - 1]:
                k += 1
            else:
                result[index - k - 1] = team
                count += 1
        count = 0
        k = 0
        while index + k + 1 < N and count < K:
            if result[index + k + 1]:
                k += 1
            else:
                result[index + k + 1] = team
                count += 1
        team ^= 3
    print(*result, sep='')
