if __name__ == "__main__":
    T = int(input())
    for t in range(T):
        N = int(input())
        left, right = 0, 0
        power = 0
        while N:
            now = N % 10
            if now == 4:
                left += 2 * (10 ** power)
                right += 2 * (10 ** power)
            else:
                left += now * (10 ** power)
            power += 1
            N = N // 10
        print('Case #{}: {} {}'.format(t+1, left, right))

            