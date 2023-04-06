from typing import List
from collections import defaultdict

# 12.03 first try自己写出来了。但是一开始用set不行，得用list，因为不需要去重。
# T O(nklogk), klogk for sorting, n for length of strs. M O(nk)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for word in strs:
            tpl = tuple(sorted(word))
            if tpl in res:
                res[tpl].append(word)
            else:
                res[tpl] = [word]

        return res.values()


# neet code的解法，他用的hash key是一个26位的tuple，然后每个字母出现一次就在那个index上+1
# 他这个的时间复杂度更好
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for c in word:
                count[ord(c) - ord("a")] += 1
            res[tuple(count)].append(word)
        
        return res.values()


# T O(nk), M O(nk). n is length of strs, k is length of longest word
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_hash = defaultdict(list)
        for w in strs:
            count = [0] * 26
            for c in w:
                count[ord(c) - ord("a")] += 1
            str_hash[tuple(count)].append(w)
        
        return list(str_hash.values()) # 不需要再转化一遍list
        