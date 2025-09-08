from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            if carry == 1 and digits[i] == 9:
                digits[i] = 0
            elif carry == 1 and digits[i] < 9:
                digits[i] += 1
                carry = 0
        if carry == 1:
            digits.insert(0, 1)

        return digits
