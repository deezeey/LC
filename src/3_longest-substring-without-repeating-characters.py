# 10.03 first try，T和M都不错
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        length = 1
        sub_string = s[0]
        for c in s[1:]:
            if c not in sub_string:
                sub_string += c
            else:
                sub_string = sub_string.split(c, 1)[1] + c
            length = max(length, len(sub_string))
        return length


# neetcode写法，思路一样，用了双指针
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res


# 11.03 复习自己写，思路居然错了， 碰到“"dvdf" 时候return了2，但应该是3
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        cur_str = s[0]
        i = 1
        cur_len = 1
        len_collection = []

        while i < len(s):
            if s[i] not in cur_str:
                cur_str += s[i]
                cur_len += 1
            else:
                len_collection.append(cur_len)
                cur_len = 1
                cur_str = s[i]
            i += 1

        len_collection.append(cur_len)
        
        return max(len_collection)

# 看 neet code答案又默写了一遍 T O(n) M O(n)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        cur_char = set()
        max_len = 0

        while r < len(s):
            while s[r] in cur_char:
                cur_char.remove(s[l])
                l += 1
            cur_char.add(s[r])
            max_len = max(max_len, r - l + 1)
            r += 1
        
        return max_len

# 12.14 复习自己写出来了但是一开始没有那个 for del过不了“abba”的test case
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        l = 0
        cur = {}
        for i, c in enumerate(s):
            if c not in cur:
                cur[c] = i
            else:
                for c2 in s[l:cur[c]]:
                    del cur[c2]
                l = cur[c] + 1
                cur[c] = i     
            max_len = max(max_len, i - l + 1)
        return max_len