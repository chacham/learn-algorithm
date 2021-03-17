if __name__ == "__main__":
    N, K = map(int, input().split())
    S = input()
    res = []
    for s in S:
        while res and K > 0 and res[-1] < s:
            K -= 1
            res.pop()
        res.append(s)
    while K:
        K -= 1
        res.pop()
    print("".join(res))
