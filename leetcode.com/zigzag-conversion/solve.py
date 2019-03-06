class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        arr = [[] for _ in range(numRows)]
        n, N = numRows, numRows * 2 - 2
        for i in range(len(s)):
            m = i % N
            if m < n:
                arr[m].append(s[i])
            else:
                arr[N - m].append(s[i])
        return ''.join(map(lambda arr: ''.join(arr), arr))
