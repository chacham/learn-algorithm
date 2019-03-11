def solution(arr):
    memo = {}
    def helper(arr, start, end):
        if (start, end) in memo:
            return memo[(start, end)]

        if end - start == 1:
            res = int(arr[start])
            memo[(start, end)] = res, res
            return memo[(start, end)]

        maxRes, minRes = float('-inf'), float('inf')
        for i in range(start + 1, end, 2):
            left = helper(arr, start, i)
            right = helper(arr, i+1, end)
            if arr[i] == '+':
                maxRes = max(maxRes, left[0] + right[0])
                minRes = min(minRes, left[1] + right[1])
            else:
                maxRes = max(maxRes, left[0] - right[1])
                minRes = min(minRes, left[1] - right[0])
        memo[(start, end)] = maxRes, minRes
        return memo[(start, end)]
    return helper(arr, 0, len(arr))[0]
