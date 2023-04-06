from typing import List
from collections import defaultdict
from math import atan2
# 3.2 first try. 自己的brute force的解，能过33 /41 cases但是碰到[[0,0],[4,5],[7,8],[8,9],[5,6],[3,4],[1,1]]挂了
# 可能自己数学上没想明白，这个规则并不足以证明它们在一条线上
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # rule: y2 - y1 = N * (x2 - x1) any other point satisfies this N would be on the same line as these 2
        # we need to consider horizontal or vertial lines where we would get divided by 0 error
        # every 2 pt in arr would give us a constant N
        # do we need to find every possible N and then check the rest point?
        # [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
        # N = （2 - 1） / （3 - 1） = 0.5
        # （3 - 1）/ （5 - 1） = 0.5, check
        # (1 - 1) / (4 - 1) = 0, bad
        # (3 - 1) / (2 - 1) = 2, bad
        # (4 - 1) / (1 - 1) = division error, bad
        # what if we get min & max of x and y first, we get the N and calc all possible pts?
        # we can calc diff Ns: there will be len(points) * (len(point) - 1) / 2 possibilities
        N = len(points)
        if N == 1:
            return 1
        angles = defaultdict(set)
        for i in range(N - 1):
            xi, yi = points[i]
            j = i + 1
            while j < N:
                xj, yj = points[j]
                if xi == xj:
                    angles['vertical' + str(xj)].update({i, j})
                else:
                    a = str((yj - yi) / (xj - xi))
                    angles[a].update({i, j})
                j += 1
        print(angles)
        return max([len(pt) for pt in angles.values()])

# 想了想记起来斜率 + intercept才能define一个线，加上intercept做key能过，但是TM没有那么理想
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # rule: y2 - y1 = N * (x2 - x1) any other point satisfies this N would be on the same line as these 2
        # we need to consider horizontal or vertial lines where we would get divided by 0 error
        # every 2 pt in arr would give us a constant N
        # do we need to find every possible N and then check the rest point?
        # [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
        # N = （2 - 1） / （3 - 1） = 0.5
        # （3 - 1）/ （5 - 1） = 0.5, check
        # (1 - 1) / (4 - 1) = 0, bad
        # (3 - 1) / (2 - 1) = 2, bad
        # (4 - 1) / (1 - 1) = division error, bad
        # what if we get min & max of x and y first, we get the N and calc all possible pts?
        # we can calc diff Ns: there will be len(points) * (len(point) - 1) / 2 possibilities
        N = len(points)
        if N == 1:
            return 1
        angles = defaultdict(set)
        for i in range(N - 1):
            xi, yi = points[i]
            j = i + 1 #因为我记录的是点，而且是universal dict所以可以从i+1开始
            while j < N:
                xj, yj = points[j]
                if xi == xj:
                    angles['vertical' + "_" + str(xj)].update({i, j})
                else:
                    a = round((yj - yi) / (xj - xi), 4)
                    intercept = yj - (a * xj)
                    angles[str(a) + "_" + str(intercept)].update({i, j})
                j += 1
        return max([len(pt) for pt in angles.values()])
    
# 官方写法直接用的atan2做key，并且不计点的idx直接计算cnt
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n == 1:
            return 1
        result = 2
        for i in range(n):
            cnt = defaultdict(int)
            for j in range(n): #注意这里不可以从i + 1开始，因为cnt是在这个i的loop里的
                if j != i:
                    cnt[atan2(points[j][1] - points[i][1],
                                   points[j][0] - points[i][0])] += 1
            result = max(result, max(cnt.values()) + 1)
        return result

# 尝试了按官网那样记录cnt而不计idx，试了很多遍经常出现floating representation error。后来发现比起round() func, 直接用format更靠谱
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        if N == 1:
            return 1
        res = 2
        for i in range(N):
            xi, yi = points[i]
            angles = defaultdict(int)
            for j in range(N):
                if i != j:
                    xj, yj = points[j]
                    if xi == xj:
                        angles['vertical' + "_" + str(xj)] += 1
                    else:
                        a = (yj - yi) / (xj - xi)
                        intercept = yj - (a * xj)
                        angles["{:.8f}".format(a) + "_" + "{:.8f}".format(intercept)] += 1
            # print(angles)
            res = max(res, max(angles.values()) + 1)
        return res