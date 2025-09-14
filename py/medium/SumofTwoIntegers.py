class Solution:
    def getSum(self, a: int, b: int) -> int:
        res, carry = 0, 0
        for i in range(32):
            first_bit, second_bit = (a & 1), (b & 1)
            current_bit = carry ^ first_bit ^ second_bit
            carry = (
                (first_bit & second_bit) | (first_bit & carry) | (second_bit & carry)
            )
            res |= current_bit << i
            a >>= 1
            b >>= 1

        if res >= 2**31:
            return res - 2**32
        return res
