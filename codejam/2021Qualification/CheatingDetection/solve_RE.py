import math

if __name__ == "__main__":
    T = int(input())
    for t in range(T):
        P = int(input())
        SCORES = [[int(x) for x in input()] for _ in range(100)]

        eQ = [0] * 10000
        for SCORE in SCORES:
            for i, s in enumerate(SCORE):
                eQ[i] += s
        for i in range(10000):
            eQ[i] = 1 / eQ[i] * 100 - 1

        eS = [0] * 100
        for i, SCORE in enumerate(SCORES):
            sumScore = sum(SCORE)
            eS[i] = 1 / (1 / sumScore * 10000 - 1)

        suspicious = [0] * 100
        for i, SCORE in enumerate(SCORES):
            for j, s in enumerate(SCORE):
                suspicious[i] += 2 ** (1 - abs(1 / (1 + eQ[j] / eS[i]) - s))
        
        res = sorted(enumerate(suspicious), key=lambda x: x[1])

        print(f"Case #{t+1}: {res[-1][0] + 1}")
