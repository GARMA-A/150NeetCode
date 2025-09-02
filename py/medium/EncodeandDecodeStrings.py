from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        """
        Input: ["neet","code","love","you"]
        neet:;code:;love:;you:;
        """
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s

        return encoded

    def decode(self, s: str) -> List[str]:
        current_str, size_str, size_num, ans = "", "", 0, []
        i = 0
        while i < len(s):
            current_str = ""
            size_str = ""
            while s[i] != "#":
                size_str += s[i]
                i += 1
            i += 1
            size_num = int(size_str)
            current_str = s[i : i + size_num]
            ans.append(current_str)
            i += size_num

        return ans
