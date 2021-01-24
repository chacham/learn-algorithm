def solve(S):
    def parse(S):
        def inner(stack):
            s = stack.pop()
            if s in ['b', 'w']:
                return s
            return [inner(stack), inner(stack), inner(stack), inner(stack)]
        return inner(list(reversed(S)))

    def rec(Ss):
        if Ss in ['b', 'w']:
            return Ss
        UL, UR, DL, DR = [rec(s) for s in Ss]
        return 'x' + ''.join([DL, DR, UL, UR])

    return rec(parse(S))

if __name__ == "__main__":
    C = int(input())
    for c in range(C):
        S = input()
        print(solve(S))
