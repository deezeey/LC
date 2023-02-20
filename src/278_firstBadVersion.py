# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    pass

# 9.29 first try, 二分的思路是对的但是running overtime，while loop有问题
class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = n // 2
        r = n
        prev_l = l
        while l < r:
            if isBadVersion(l):
                if not isBadVersion(l-1):
                    return l
                else:
                    l = prev_l
                    r = l - 1
            else:
                prev_l = l
                l = (r-l) // 2
                

# 九章正确解法，首先我上面写法的错误就是只有2个var但我们需要左中右3个var
class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n
        while l + 1 < r: # <---考虑最后情况l,mid,r连在一起，所以我们要保证l + 1 < r, 这样才有mid的位置
            mid = l + (r - l) // 2 # <-----同理只有 l + 1 < 2，我们才能保证这里不会出现分数
            if isBadVersion(mid):
                r = mid
            else:
                l = mid
        if isBadVersion(l):
        # 因为上面while loop最后一定把l或者r设置成了mid，所以最后我们只会有两个数，l,r是连在一起的。所以我们只要确认是 11， 还是 01就可以了
            return l
        return r


# 11.03 复习自己写，居然没写出来。。。因为不知道要check两个数的binary search怎么搞。看了下答案才写出来的
class Solution:
    def firstBadVersion(self, n: int) -> int:
        if n == 1:
            return n

        l, r = 1, n

        while l + 1 < r: # 这样保证了l, r之间有至少1个数
            mid = l + (r - l) // 2
            if isBadVersion(mid):
                r = mid
            else:
                l = mid
            print(l, r)
                
        if isBadVersion(l):
            return l

        return r


# 12.12 复习自己写，这回7分钟搞定
class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 0, n
        while l <= r:
            mid = (l + r) // 2
            if isBadVersion(mid):
                if mid == 0 or (mid > 0 and not isBadVersion(mid - 1)):
                    return mid
                else:
                    r = mid - 1
            else:
                l = mid + 1