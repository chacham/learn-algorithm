COUNT = 'COUNT'
END = 'END'
def solve(N, S):
    trie = { COUNT: 0 }
    for s in S:
        nowTrie = trie
        for c in reversed(s):
            if c not in nowTrie:
                nowTrie[c] = { COUNT: 0 }
            nowTrie[COUNT] += 1
            nowTrie = nowTrie[c]
        nowTrie[COUNT] += 1
        nowTrie[END] = True
    def helper(trie):
        res = 0
        for k in trie:
            if k in [END, COUNT]:
                continue
            if trie[k][COUNT] >= 2:
                res += helper(trie[k])
        if trie[COUNT] - res >= 2:
            res += 2
        return res

    res = 0
    for k in trie:
        if k in [END, COUNT]:
            continue
        res += helper(trie[k])
    return res

if __name__ == "__main__":
    T = int(input())
    for t in range(T):
        N = int(input())
        S = [input() for _ in range(N)]
        print("Case #{}: {}".format(t+1, solve(N, S)))
