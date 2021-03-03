class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        mergedB = [0] * 26
        for b in B:
            tmpB = [0] * 26
            for c in b:
                tmpB[ord(c) - ord('a')] += 1
            for i in range(26):
                mergedB[i] = max(mergedB[i], tmpB[i])
        res = []
        for a in A:
            tmpA = [0] * 26
            for c in a:
                tmpA[ord(c) - ord('a')] += 1
            for i in range(26):
                if tmpA[i] < mergedB[i]:
                    break
            else:
                res.append(a)
        return res
