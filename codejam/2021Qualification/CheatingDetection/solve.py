import math

if __name__ == "__main__":
    T = int(input())
    for t in range(T):
        P = int(input())
        SCORES = [[int(x) for x in input()] for _ in range(100)]
        SUM_SCORES = [sum(scores) for scores in SCORES]
        # usableScores = [x[1] for x in enumerate(SUM_SCORES)[10:90]]

        pQ = [0] * 10000
        for i in range(len(SCORES)):
            pQ[i] = SUM_SCORES[i] / 100
        
        pS = [0] * 100
        for i, SCORE in enumerate(SCORES):
            for j in range(10000):
                pS[i] += SCORE[j]
            pS[i] /= 10000

        suspicious = [0] * 100
        for i, SCORE in enumerate(SCORES):
            for j, s in enumerate(SCORE):
                prob = pQ[j] * pS[i]
                suspicious[i] += 10 ** abs(s - prob)
        
        res = max(enumerate(suspicious), key=lambda x: x[1])

        print(f"Case #{t+1}: {res[0] + 1}")
