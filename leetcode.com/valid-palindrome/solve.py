class Solution:
    def isPalindrome(self, s: str) -> bool:
        lst = [c for c in filter(lambda x: x.isalnum(), s.lower())]
        return ''.join(lst) == ''.join(reversed(lst))
