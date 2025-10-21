class Solution:
    def scoreBalance(self, s: str) -> bool:
        n = len(s)
        if n==1:
            return False
        prefix = [0] *(n+1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + ord(s[i]) - ord("a") + 1

        print(prefix)
        for i in range(1, n):
            if prefix[i] == prefix[n] - prefix[i]:
                return True

        return False





