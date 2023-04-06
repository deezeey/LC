from typing import List
# 2.7 first try
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = [0] * n
        for i in range(n):
            if (i + 1) % 5 == 0 and (i + 1) % 3 == 0:
                res[i] = "FizzBuzz"
                continue
            if (i + 1) % 3 == 0:
                res[i] = "Fizz"
                continue
            if (i + 1) % 5 == 0:
                res[i] = "Buzz"
                continue
            res[i] = str(i + 1)
        return res