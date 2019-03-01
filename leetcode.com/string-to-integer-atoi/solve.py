class Solution:
    def myAtoi(self, str: str) -> int:
        LEN = len(str)
        INT_MAX, INT_MIN = (1 << 31) - 1, -1 * (1 << 31)

        sign, num = 0, 0

        i = 0
        while i < LEN and str[i].isspace():
            i += 1

        if i < LEN and str[i] in '+-':
            if str[i] == '-':
                sign = 1
            i += 1

        while i < LEN and str[i].isnumeric():
            num *= 10
            num += int(str[i])
            i += 1

        if sign:
            num *= -1

        if num < INT_MIN:
            return INT_MIN
        if num > INT_MAX:
            return INT_MAX
        return num
