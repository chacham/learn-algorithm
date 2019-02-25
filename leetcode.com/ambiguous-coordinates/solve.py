class Solution:
    def ambiguousCoordinates(self, S):
        def checkInt(s):
            if not s:
                return False
            if len(s) > 1 and s[0] == '0':
                return False
            return True
        def checkFrac(s):
            if s and s[-1] == '0':
                return False
            return True
        res = []
        S = S[1:-1]
        # aInt i aFrac j bInt k bFrac
        # 1 < i <= j < k <= len(S)-2
        for i, j, k in [
            (i, j, k)
            for i in range(0, len(S))
            for j in range(i, len(S))
            for k in range(j+1, len(S) + 1)
        ]:
            aInt, aFrac, bInt, bFrac = S[:i], S[i:j], S[j:k], S[k:]
            if checkInt(aInt) and checkFrac(aFrac) and checkInt(bInt) and checkFrac(bFrac):
                if aFrac and bFrac:
                    res.append('({}.{}, {}.{})'.format(aInt, aFrac, bInt, bFrac))
                elif aFrac:
                    res.append('({}.{}, {})'.format(aInt, aFrac, bInt))
                elif bFrac:
                    res.append('({}, {}.{})'.format(aInt, bInt, bFrac))
                else:
                    res.append('({}, {})'.format(aInt, bInt))
        return res

