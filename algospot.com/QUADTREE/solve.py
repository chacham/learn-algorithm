def solve(s):
    # Returns result, restString
    if s[0] != 'x':
        return s[0], s[1:]

    subQuadtree = []
    rest = s[1:]
    for i in range(4):
        tmp, rest = solve(rest)
        subQuadtree.append(tmp)
    results = ['x'] + subQuadtree[2:] + subQuadtree[:2]
    return "".join(results), rest


if __name__ == "__main__":
    C = int(input())
    for c in range(C):
        s = input()
        print(solve(s)[0])
