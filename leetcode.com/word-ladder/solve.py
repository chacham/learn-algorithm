def ladderLength(beginWord, endWord, wordList):
    from collections import defaultdict
    trans = defaultdict(list)

    LEN = len(beginWord)
    def interWords(word):
        return [word[:i] + '*' + word[i+1:] for i in range(LEN)]

    for interWord in interWords(beginWord):
        trans[interWord].append(beginWord)
    for word in wordList:
        for interWord in interWords(word):
            trans[interWord].append(word)

    visited = set([beginWord])
    visitedInter = set()

    res = 1
    starts = [beginWord]
    while True:
        res += 1
        newVisits = set()
        newVisitedInter = set()
        for word in starts:
            for interWord in [interWord for interWord in interWords(word) if interWord not in visitedInter]:
                newVisitedInter.add(interWord)
                for nextWord in [nextWord for nextWord in trans[interWord] if nextWord not in visited]:
                    newVisits.add(nextWord)
        if not newVisits:
            return 0
        if endWord in newVisits:
            return res
        visited |= newVisits
        visitedInter |= newVisitedInter
        starts = list(newVisits)
