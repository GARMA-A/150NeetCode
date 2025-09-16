class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need, window = [0] * 26, [0] * 26
        for ch in s1:
            need[ord(ch) - ord("a")] += 1
        l = 0
        for r in range(len(s2)):
            window[ord(s2[r]) - ord("a")] += 1
            if r - l + 1 > len(s1):
                window[ord(s2[l]) - ord("a")] -= 1
                l += 1
            if need == window:
                return True

        return False
