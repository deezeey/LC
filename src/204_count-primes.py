from math import ceil, sqrt
# 2.10 first try 自己想到了一点思路，即去掉所有2，3，5，7的倍数，但是如何去重，比如6在2被算了一遍，3又被算了一遍
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        # exclude all even, there are n // 2 - 1 odd nums
        # every 3, 5, 7 steps we have something divisible by 3, 5, 7 and they need to be eliminated
        res = 0
        res += ((n // 7) + (n // 5) + (n // 3))
        return n - res

# 官方正解是两层for loop。我们选一个标的数字i，比如i=2，然后不停地把它的倍数mark成composite直到超过n，换下一个i，i=3，继续重复这个过程直到剩下都是质数。
# 外层for loop，即i的range是sqrt(n)。因为假设n是30，floor（sqrt（30）） = 5。所以i最多只用考虑到5.因为6的话你会发现6*1，6*2直到 6*5都已经在i=1~5的for loop里被考虑过了，而 6*6 > 30所以不用考虑
# 而内层for loop只用考虑i * i，i * (i+1)...直到超过n，因为 i * （1 ～ i-1）都已经在前面被考虑过了。比如还是上面那个案例，
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        
        # Initialize numbers[0] and numbers[1] as False because 0 and 1 are not prime.
        # Initialze numbers[2] through numbers[n-1] as True because we assume each number
        # is prime until we find a prime number (p) that is a divisor of the number
        numbers = [False, False] + [True] * (n - 2)
        for p in range(2, int(sqrt(n)) + 1):
            if numbers[p]:
                # Set all multiples of p to false because they are not prime.
                for multiple in range(p * p, n, p):
                    numbers[multiple] = False
        
        # numbers[index] will only be true where index is a prime number
        # return the number of indices whose value is true.
        return sum(numbers)

class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        res = [True] * n
        res[0], res[1] = False, False
        for x in range(2, ceil(sqrt(n))):
            if res[x]:
                y = x
                while x * y < n: # 这一行官方写的 for multiple in range(p * p, n, p): 更好
                    res[x * y] = False
                    y += 1
        return res.count(True)