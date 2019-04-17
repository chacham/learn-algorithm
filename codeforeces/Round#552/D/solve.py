if __name__ == "__main__":
    N, B, A = map(int, input().split())
    S = [True if x == "1" else False for x in input().split()]

    b, a = B, A
    result = 0
    for i in range(N):
        if a == 0 and b == 0:
            break
        elif a == 0: # b > 0 and a = 0
            b -= 1
            if S[i]:
                a = min(a + 1, A)
        elif b == 0: # a > 0 and b = 0
            a -= 1
        else: # Both > 0
            if S[i] and a < A:
                b -= 1
                a += 1
            else:
                a -= 1
        result += 1
    print(result)
