class Solution:
    def reverseBits(self, n: int) -> int:
        reversed_n = 0
        for i in range(32):
            bit = (n >> i) & 1
            reversed_n += bit << (31 - i)
        return reversed_n
