def convert(S):
    res = []
    for i in range(0, len(S), 64):
        s = S[i:i+64]
        s += (64 - len(s)) * 'F'
        b = "".join(["1" if c == 'M' else "0" for c in s])
        # print(s, b)
        n = int(b, 2)
        res.append(n)
    return res

def lshiftAnd(a, b, shift):
    return a & (b << shift)

def rshiftAnd(a, b, shift):
    return a & (b >> shift)

def solve(MEMBERS, FANS):
    MEMbits = convert(MEMBERS)
    FANbits = convert(FANS)
    res = 0
    for i in range(len(FANS) - len(MEMBERS) + 1):
        base = i // 64
        lshift = i % 64
        rshift = 64 - lshift
        for j in range(len(MEMbits)):
            if lshiftAnd(MEMbits[j], FANbits[base + j], lshift):
                break
            if rshift and j < len(MEMbits) - 1 and rshiftAnd(MEMbits[j+1], FANbits[base + j], rshift):
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
