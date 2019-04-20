class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        # def normalize(s):
        #     even = sorted(s[::2])
        #     odd = sorted(s[1::2])
        #     res = []
        #     for i in range(len(odd)):
        #         res.append(even[i])
        #         res.append(odd[i])
        #     if len(even) > len(odd):
        #         res.append(even[-1])
        #     return ''.join(res)
        # return len(set(map(normalize, A)))

        def normalize(s):
            return (''.join(sorted(s[::2])), ''.join(sorted(s[1::2])))
        return len({normalize(s) for s in A})
