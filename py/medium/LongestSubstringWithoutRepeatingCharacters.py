class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        ans = 0
        count = set()
        while r < len(s):
            if s[r] not in count:
                count.add(s[r])
                ans = max(ans, (r - l) + 1)
                r += 1
            else:
                count.remove(s[l])
                l += 1

        return ans
