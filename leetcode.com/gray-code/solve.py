class Solution:
    def grayCode(self, n: int) -> 'List[int]':
        if n == 0:
            return [0]
        children = self.grayCode(n - 1)
        msb = 1 << (n - 1)
        return children + [*map(lambda x: x + msb, reversed(children))]
