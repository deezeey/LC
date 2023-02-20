from typing import List

# 2.6 first try写出来了但是可能可以写的更简洁？
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        n = 1
        res = []
        while n <= numRows:
            if n == 1:
                res.append([1])
            elif n == 2:
                res.append([1, 1])
            else:
                cur = [0] * n
                cur[0], cur[-1] = 1, 1
                up_level = res[-1]
                i, l, r = 1, 0, 1
                while i  < n - 1 and r < len(up_level):
                    cur[i] = up_level[l] + up_level[r]
                    l = r
                    r += 1
                    i += 1
                res.append(cur)
            n += 1
        return res

# neetcode写的我觉得也没有很简洁
class Solution:
    def generate(self, rowIndex) -> List[List[int]]:
        if rowIndex == 0:
            return [[1]]
        else:
            return self.getAllRow(rowIndex - 1)

    def getAllRow(self, rowIndex):
        if rowIndex == 0:
            return [[1]]
        ListPrec = self.getAllRow(rowIndex - 1)
        Len = len(ListPrec[-1])
        ListPrec.append([1])
        for i in range(0, Len - 1):
            ListPrec[-1].append(ListPrec[-2][i] + ListPrec[-2][i + 1])
        ListPrec[-1].append(1)
        return ListPrec