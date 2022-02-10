import re

def solve(S):
    p = re.compile("^(100+1+|01)+$")
    return p.match(S) and True

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        if solve(input()):
            print("YES")
        else:
            print("NO")
