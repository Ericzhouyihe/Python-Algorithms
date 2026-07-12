class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = [char.lower() for char in s if char.isalnum()]
        new_s = ''.join(clean_s)
        return new_s == new_s[::-1]
