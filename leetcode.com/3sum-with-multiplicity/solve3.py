class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        count = [0] * 101
        for n in arr:
            count[n] += 1

        res = 0

        if target % 3 == 0 and count[target//3] >= 3:
            cnt = count[target//3]
            res += cnt * (cnt-1) * (cnt-2) // 6

        for n in range(101):
            m = target - n * 2
            if 0 <= m < 101 and n != m:
                res += count[n] * (count[n]-1) // 2 * count[m]

        for l in range(101):
            for m in range(l+1, 101):
                r = target - l - m
                if m < r < 101:
                    res += count[l] * count[m] * count[r]

        return res % (10**9 + 7)
