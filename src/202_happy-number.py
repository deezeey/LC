
# 1.25 first try，这个过不了n = 1111111的case
class Solution:
    def isHappy(self, n: int) -> bool:
        total = 0
        for c in str(n):
            total += int(c) ** 2
        if total < 10:
            return True if total == 1 else False
        else:
            return self.isHappy(total)

# 正解居然是快慢指针？
class Solution:
    def isHappy(self, n: int) -> bool:
        def squareSum(n):
            total = 0
            while n:
                total += (n % 10) ** 2
                n = n // 10
            return total

        slow, fast = n, squareSum(n)
        while slow != fast:
            fast = squareSum(fast) #fast每个循环要算两次
            fast = squareSum(fast)
            slow = squareSum(slow) #slow每个循环要算1次
        
        # 及时答案是1 while loop也会结束，因为1 ** 2永远=1所以快慢指针最后都会停在1
        # 但如果在一个不是1的数loop住了那么就不是happy number
        return True if fast == 1 else False