class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r, max_repeating_char, arr = 0, 0, 0, [0] * 26
        ans = 0
        while r < len(s):
            arr[ord(s[r]) - 65] += 1
            max_repeating_char = max(arr)
            if ((r - l + 1) - max_repeating_char) > k:
                arr[ord(s[l]) - 65] -= 1
                l += 1
            else:
                ans = max(ans, (r - l + 1))
            r += 1

        return ans
