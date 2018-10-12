import math

MOD = 1000000007

def devisor(N):
    left = []
    right = []
    for i in range(1, 1000):
        if i > N / i:
            break
        if N % i == 0:
            left.append(i)
            right.append(N // i)
    if left[-1] == right[-1]:
        left.pop()
    right.reverse()
    return left + right

if __name__ == "__main__":
    T = int(input())
    for t in range(T):
        N = int(input())
        H = [int(h) for h in input().split()]

        devisors = [devisor(h) for h in reversed(H)]

        dp = [{h: 1 for h in devisors[0]}]
        for i in range(1, len(devisors)):
            tail = devisors[i-1]
            head = devisors[i]
            dp.append({})

            tailTop = len(tail) - 1
            headTop = len(head) - 1
            acc = 0
            while headTop >= 0:
                while tailTop >= 0 and tail[tailTop] >= head[headTop]:
                    acc += dp[i-1][tail[tailTop]]
                    acc %= MOD
                    tailTop -= 1
                dp[i][head[headTop]] = acc % MOD
                headTop -= 1
        print(sum(dp[-1].values()) % MOD)

