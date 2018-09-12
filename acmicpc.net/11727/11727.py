def solve(N):
    if N == 1:
        return 1
    if N == 2:
        return 3
    bfbf = 1
    bf = 3
    for i in range(3, N):
        bfbf, bf = bf, (bfbf * 2 + bf) % 10007
    return (bfbf * 2 + bf) % 10007
        
if __name__ == "__main__":
    N = int(input())
    print(solve(N))