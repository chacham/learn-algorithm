class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mCounts = {}
        for c in magazine:
            if c not in mCounts:
                mCounts[c] = 0
            mCounts[c] += 1
        rCounts = {}
        for c in ransomNote:
            if c not in rCounts:
                rCounts[c] = 0
            rCounts[c] += 1
        print(mCounts, rCounts)
        for c in rCounts:
            if c not in mCounts or mCounts[c] < rCounts[c]:
                return False
        return True
        