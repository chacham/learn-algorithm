class Solution:
    def trap(self, height):
        asc, desc = [0], [len(height) - 1]

        for i in range(len(height)):
            if height[i] >= height[asc[-1]]:
                asc.append(i)

        for i in reversed(range(asc[-1], len(height))):
            if height[i] > height[desc[-1]]:
                desc.append(i)
        desc.reverse()

        res = 0
        
        for i in range(1, len(asc)):
            left, right = asc[i-1], asc[i]
            h = height[left] # asc. left if lower
            for j in range(left+1, right):
                res += h - height[j]

        for i in range(1, len(desc)):
            left, right = desc[i-1], desc[i]
            h = height[right] # desc. right is lower
            for j in range(left+1, right):
                res += h - height[j]

        return res
