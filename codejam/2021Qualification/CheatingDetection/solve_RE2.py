import math

if __name__ == "__main__":
    T = int(input())
    for t in range(T):
        P = int(input())
        SCORES = [[int(x) for x in input()] for _ in range(100)]

        sumScores = sorted([(sum(scores), i) for i, scores in enumerate(SCORES)])
        usableScores = [x[1] for x in sumScores[10:90]]

        pQ = [0] * 10000
        eQ = [0] * 10000
        Q = [0] * 10000
        usableQ = []
        for i in usableScores:
            for j, s in enumerate(SCORES[i]):
                pQ[j] += s
        for i in range(10000):
            pQ[i] = pQ[i] / len(usableScores)
            eQ[i] = max(1 / pQ[i] - 1, 0.01)
            Q[i] = math.log(eQ[i])
            if -1 < Q[i] < 1:
                usableQ.append(i)
        
        pS = [0] * 100
        eS = [0] * 100
        # S = [0] * 100
        for i, SCORE in enumerate(SCORES):
            for j in usableQ:
                pS[i] += SCORE[j]
            pS[i] /= len(usableQ)
            eS[i] = 1 / max(1 / pS[i] - 1, 0.01)
            # S[i] = math.log(eS[i])

        suspicious = [0] * 100
        for i, SCORE in enumerate(SCORES):
            for j, s in enumerate(SCORE):
                prob = 1 / (1 + eQ[j] / eS[i])
                suspicious[i] += 10 ** abs(s - prob)
                # suspicious[i] += 2 ** (1 - abs(1 / (1 + eQ[j] / eS[i]) - s))
        
        res = sorted(enumerate(suspicious), key=lambda x: x[1])
        print(res)

        print(f"Case #{t+1}: {res[-1][0] + 1}")
