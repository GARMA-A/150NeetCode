class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars_of_s = ""
        for ch in s:
            if ch.isspace() or not ch.isalnum():
                continue
            else:
                chars_of_s += ch.lower()

        l, r = 0, len(chars_of_s) - 1
        while l <= r:
            if chars_of_s[l] != chars_of_s[r]:
                return False
            l += 1
            r -= 1

        return True
