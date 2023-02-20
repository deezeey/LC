from typing import List

# 自己20分钟写了一个大概的算法，我知道greedy的一般都会很简单，所以没写代码因为我的思路应该是只对了一半
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # make a dict of dict --> {0:{1:(2), 2:(0, 1), 5:(3)}, 1:{2:(2, 3), 3:(1), 5:(0)}, 2:{...}}
        # {0/1/2:{distinct_val we have at the idx: (idx of triplet containing this value in triplets)}}
        # looking at the target, get the idx of triplet matches the number at position 0/1/2 respectively
        # it would look like {0:(3), 1:(0), 2(2, 4)}
        # start from the smallest set, do a greedy search, 
        # if running out of all the elment in the set and we can't find any match, return False immediately
        # else if we are able to get the target, return True
        pass

# 看了neetcode思路自己写的，写的还是太复杂
# 思路是如果有一个triplet任何一位大于target的同位置数字，这个triplet可以被排除
# 另外最重要的第二点是，当排除以上triplets之后，剩下的triplets里面，只要target每个位置的数字，存在于至少一个triplet中，那么我们一定可以置换到完整的target，
# 因为所有这些triplets里面这个位置的数字，都会小于等于target数字
# 我自己的思路kind of想到了第二点的前半，但没想到第一点。
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = set()
        for j in range(len(triplets)):
            t = triplets[j]
            if all(t[i] <= target[i] for i in range(3)):
                good.add(j)
        res = [False] * 3
        for g_idx in good:
            for k in range(3):
                if triplets[g_idx][k] == target[k]:
                    res[k] = True
                    continue
        return all(res)

# neetcode写的比我简单很多
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = set()

        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            for i, v in enumerate(t):
                if v == target[i]:
                    good.add(i) #注意这里加的i是t的index，即[0,1,2]之一
        return len(good) == 3 # len == 3 代表target的3个位置都有满足条件的数字在good里