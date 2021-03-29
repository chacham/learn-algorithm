import math

if __name__ == "__main__":
    T = int(input())
    for t in range(T):
        P = int(input())
        SCORES = [[int(x) for x in input()] for _ in range(100)]

        sumScores = sorted([(sum(scores), i) for i, scores in enumerate(SCORES)])
        usableScores = [x[1] for x in sumScores[10:90]]

        pQ = [0] * 10000
        usableQ = []
        for i in usableScores:
            for j, s in enumerate(SCORES[i]):
                pQ[j] += s
        for i in range(10000):
            pQ[i] = pQ[i] / len(usableScores)
            if 0.2 < pQ[i] < 0.8:
                usableQ.append(i)
        
        pS = [0] * 100
        for i, SCORE in enumerate(SCORES):
            for j in usableQ:
                pS[i] += SCORE[j]
            pS[i] /= len(usableQ)

        suspicious = [0] * 100
        for i, SCORE in enumerate(SCORES):
            for j, s in enumerate(SCORE):
                prob = pQ[j] * pS[i]
                suspicious[i] += 10 ** abs(s - prob)
        
        res = sorted(enumerate(suspicious), key=lambda x: x[1])

        print(f"Case #{t+1}: {res[-1][0] + 1}")
