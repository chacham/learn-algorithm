if __name__ == "__main__":
    N = int(input())
    score = [[0, 0, 0, 0] for i in range(3)]

    for n in range(N):
        a, b, c = map(int, input().split())

        score[0][0] += a
        score[0][a] += 1

        score[1][0] += b
        score[1][b] += 1

        score[2][0] += c
        score[2][c] += 1

    tot_score = [x[0] for x in score]
    max_score = max(tot_score)
    candidates = [c for c in [0, 1, 2] if tot_score[c] == max_score]

    for i in range(3, 0, -1):
        if len(candidates) == 1:
            break
        max_score_count = max([score[c][i] for c in candidates])
        nextCandidates = [c for c in candidates]
        for c in candidates:
            if score[c][i] != max_score_count:
                nextCandidates.remove(c)
        candidates = nextCandidates

    if len(candidates) == 1:
        print(candidates[0] + 1, max_score)
    else:
        print(0, max_score)
