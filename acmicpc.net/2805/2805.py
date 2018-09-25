if __name__ == "__main__":
    N, M = map(int, input().split())
    trees = [int(x) for x in input().split()]
    trees = sorted(trees, reverse=True)

    count = 0
    total = 0
    for i in range(1, len(trees)):
        total += (trees[i-1] - trees[i]) * i
        if total >= M:
            count = i
            break
    else:
        total += trees[-1] * len(trees)
        count = len(trees)
    
    top = trees[count - 1]
    bottom = 0 if len(trees) == count else trees[count]
    base = bottom * count

    while True:
        mid = (top + bottom) // 2
        if mid == bottom:
            break
        elif total - (mid * count - base) >= M:
            bottom = mid
        else:
            top = mid

    print(bottom)
    