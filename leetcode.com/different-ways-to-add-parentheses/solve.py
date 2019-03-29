class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        memo = {'': [0]}
        def helper(s):
            if s in memo:
                return memo[s]
            if s.isdecimal():
                memo[s] = [int(s, 10)]
                return memo[s]

            result = []
            for i in range(0, len(s)-1):
                if s[i] == "-":
                    for l, r in [(l, r) for l in helper(s[:i]) for r in helper(s[i+1:])]:
                        result.append(l-r)
                if s[i] == "+":
                    for l, r in [(l, r) for l in helper(s[:i]) for r in helper(s[i+1:])]:
                        result.append(l+r)
                if s[i] == "*":
                    for l, r in [(l, r) for l in helper(s[:i]) for r in helper(s[i+1:])]:
                        result.append(l*r)
            memo[s] = result
            return memo[s]

        return sorted(helper(input))
