class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        count = [0] * 101
        for n in arr:
            count[n] += 1

        res = 0

        if target % 3 == 0 and count[target//3] >= 3:
            cnt = count[target//3]
            res += cnt * (cnt-1) * (cnt-2) // 6

        for l in range(101):
            for r in range(l+1, 101):
                if (l*2 + r) == target and count[l] >= 2 and count[r] >= 1:
                    res += count[l] * (count[l]-1) // 2 * count[r]
                if (l + r*2) == target and count[l] >= 1 and count[r] >= 2:
                    res += count[l] * count[r] * (count[r]-1) // 2

        for l in range(101):
            for m in range(l+1, 101):
                r = target - l - m
                if m < r < 101:
                    res += count[l] * count[m] * count[r]

        return res % (10**9 + 7)
