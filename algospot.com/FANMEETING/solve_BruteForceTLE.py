def solve(MEMBERS, FANS):
    res = 0
    for i in range(len(FANS) - len(MEMBERS) + 1):
        for j in range(len(MEMBERS)):
            if MEMBERS[j] == 'M' and FANS[j + i] == 'M':
                break
        else:
            res += 1
    return res


if __name__ == "__main__":
    C = int(input())
    for _ in range(C):
        MEMBERS = input()
        FANS = input()
        print(solve(MEMBERS, FANS))
