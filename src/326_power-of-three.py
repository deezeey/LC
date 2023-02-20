# 2.7 first try, 这个是比较intuitive的方法
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        def powOf3(num):
            if num == 1:
                return True
            if num <= 0 or 1 < num < 3:
                return False
            return powOf3(num / 3)
        return powOf3(n)

# 还有一个方法是base conversion。比如在2进制中，2的2次方，也就是4，写作100， 2的3次方也就是8，写作1000
# 同理只要我们把数字从十进制转化成3进制，只要他的表达是1加上若干个0，那么他就一定是3的次方数
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        base3 = self.convertToBase(n, 3)
        # print(base3)
        return base3[0] == 1 and all([base3[i] == 0 for i in range(1, len(base3))])

    def convertToBase(self, n: int, b: int):
        res = []
        if n == 0:
            return [0]
        while n:
            res.append(n % b)
            n //= b
        return res[::-1]