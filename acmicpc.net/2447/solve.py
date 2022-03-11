mem = {
    3: [
            "***",
            "* *",
            "***",
    ]
}

def solve(N):
    def merge(l, m, r):
        return [a + b + c for a, b, c in zip(l, m, r)]
    def empty(N):
        return [" " * N for _ in range(N)]

    if N in mem:
        return mem[N]
        
    mem[N] = [
        *merge(solve(N//3), solve(N//3), solve(N//3)), 
        *merge(solve(N//3), empty(N//3), solve(N//3)), 
        *merge(solve(N//3), solve(N//3), solve(N//3)), 
    ]
    return mem[N]

if __name__ == "__main__":
    N = int(input())
    print(*solve(N), sep='\n')
