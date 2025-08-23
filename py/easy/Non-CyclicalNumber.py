from collections.abc import Set


class Solution:
    def isHappy(self, n: int) -> bool:
        st = set()
        while n != 1:
            if n in st:
                return False
            else:
                st.add(n)
            n = self.sumOfDigits(n)

        return True

    def sumOfDigits(self, n: int) -> int:
        ans = 0
        while n > 0:
            digit = (n % 10) ** 2
            ans += digit
            n //= 10
        return ans
