def convert(S):
    b = "".join(["1" if c == 'M' else "0" for c in S])
    return int(b, 2)

def solve(MEMBERS, FANS):
    MEMbits = convert(MEMBERS)
    FANbits = convert(FANS)
    res = 0
    for i in range(len(FANS) - len(MEMBERS) + 1):
        if MEMbits & (FANbits >> i):
            continue
        else:
            res += 1
    return res

if __name__ == "__main__":
    C = int(input())
    for _ in range(C):
        MEMBERS = input()
        FANS = input()
        print(solve(MEMBERS, FANS))
