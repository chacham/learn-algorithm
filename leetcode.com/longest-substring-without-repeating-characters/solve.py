class Solution:
    def lengthOfLongestSubstring(self, s: 'str') -> 'int':
        maxLen = 0
        existing = {}
        first = 0
        for last in range(len(s)):
            if s[last] not in existing or existing[s[last]] == 0:
                existing[s[last]] = 1
                maxLen = max(maxLen, last - first + 1)
            else: # s[last] already exist
                while s[first] != s[last]:
                    existing[s[first]] -= 1
                    first += 1
                first += 1
        return maxLen