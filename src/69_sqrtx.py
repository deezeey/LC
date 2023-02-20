# 2.6 first try一开始隐约想到了 sqrt2一定比 //2小，但是没想到binary search
class Solution:
    def mySqrt(self, x):
        if x < 2:
            return x
        
        left, right = 2, x // 2
        
        while left <= right:
            pivot = left + (right - left) // 2 # 这里是为了防止integer overflow才这么， 其实（left + right） // 2 也行但是就怕加出一个特别大的数字来
            num = pivot * pivot
            if num > x:
                right = pivot -1
            elif num < x:
                left = pivot + 1
            else:
                return pivot
            
        return right # 我自己写了一遍怎么也没想到为啥这里最后要return right？
        # 带入 x=8试试， l=2, r=4. mid=3, 3**2=9 > 8, r = 3 - 1 = 2， l = r = mid = 2, 2 ** 2 = 4 < 8. l += 1 = 3, while loop结束

# newton's method, 纯数学题，懒得研究了
class Solution:
    def mySqrt(self, x):
        if x < 2:
            return x
        
        x0 = x
        x1 = (x0 + x / x0) / 2
        while abs(x0 - x1) >= 1:
            x0 = x1
            x1 = (x0 + x / x0) / 2        
            
        return int(x1)