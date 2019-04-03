class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        devisors = []
        aboutRoot = int(area ** 0.5) + 1
        for i in range(1, aboutRoot + 1):
            if area % i == 0:
                devisors.append(i)
        res = [devisors[-1], area // devisors[-1]]
        return sorted(res, reverse=True)
