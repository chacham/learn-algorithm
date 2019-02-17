class Solution:
    def maximumSwap(self, num: 'int') -> 'int':
        s = str(num)
        def swapAt(num, a, b):
            if a > b:
                return swapAt(num, b, a)
            return int(s[:a] + s[b] + s[a+1:b] + s[a] + s[b+1:], 10)
        
        numLength = len(str(num))
        res = num
        for i, j in [(i, j) for i in range(numLength) for j in range(i+1, numLength)]:
            res = max(res, swapAt(num, i, j))
        return res