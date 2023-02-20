from typing import List

# 1.25 first try，这题到是挺简单
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0

        for i in range(len(digits))[::-1]:
            d = digits[i]
            nu_d = d + 1 if i == len(digits) - 1 else d + carry
            if nu_d >= 10:
                carry = 1
            else:
                carry = 0
            digits[i] = nu_d % 10
            
        return digits if not carry else [1] + digits