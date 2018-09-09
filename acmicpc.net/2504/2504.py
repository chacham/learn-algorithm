def solve(S):
    def inner(start):
        if S[start] == '(' and S[start + 1] == ')':
            res, end = 2, start + 2
        elif S[start] == '[' and S[start + 1] == ']':
            res, end = 3, start + 2
        else:
            res, end = inner(start + 1)
            if S[start] == '(':
                if S[end] == ')':
                    multi = 2
            elif S[start] == '[':
                if S[end] == ']':
                    multi = 3
            else: # No match
                return -1
            res *= multi
            end += 1

        while len(S) > end and (S[end] == '(' or S[end] == '['):
            nextRes, end = inner(end)
            res += nextRes
            
        return (res, end)

    try:
        res, end = inner(0)
        if end == len(S):
            return res
        else:
            return 0
    except:
        return 0

if __name__ == "__main__":
    S = input()
    print(solve(S))
