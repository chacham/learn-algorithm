class Solution:
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        def check(w):
            already = set()
            mapping = {}
            for i, c in enumerate(w):
                if c in mapping:
                    if mapping[c] != pattern[i]:
                        return False
                elif pattern[i] in already:
                    return False
                else:
                    mapping[c] = pattern[i]
                    already.add(pattern[i])
            return True

        result = []
        for word in words:
            if check(word):
                result.append(word)
        return result
