class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        ## First implement
        # if not s and not p:
        #     return True
        # if not p:
        #     return False
        # if len(p) >= 2 and p[1] == '*':
        #     if s and (p[0] == '.' or s[0] == p[0]):
        #         return self.isMatch(s, p[2:]) or self.isMatch(s[1:], p)
        #     return self.isMatch(s, p[2:])
        # if s and p and (p[0] == '.' or s[0] == p[0]):
        #     return self.isMatch(s[1:], p[1:])
        # return False

        ## Second implement
        memo = {}
        def _helper(si, pi):
            if (si, pi) in memo:
                return memo[(si, pi)]
            if si == len(s) and pi == len(p):
                memo[(si, pi)] = True
                return True
            if pi == len(p):
                memo[(si, pi)] = False
                return False
            if pi < len(p) - 1 and p[pi+1] == '*':
                if si < len(s) and (p[pi] == '.' or s[si] == p[pi]):
                    memo[(si, pi)] = _helper(si, pi+2) or _helper(si+1, pi)
                    return memo[(si, pi)]
                memo[(si, pi)] = _helper(si, pi+2)
                return memo[(si, pi)]
            if si < len(s) and pi < len(p) and (p[pi] == '.' or s[si] == p[pi]):
                memo[(si, pi)] = _helper(si+1, pi+1)
                return memo[(si, pi)]
            return False
        return _helper(0, 0)
