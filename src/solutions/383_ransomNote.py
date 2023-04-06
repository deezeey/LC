from collections import Counter
# 9.29 first try. 自己的hash版本
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False

        def hashString(s: str) -> dict:
            sHash = {}
            for c in s:
                if c not in sHash:
                    sHash[c] = 1
                else:
                    sHash[c] += 1
            return sHash

        noteHash, magHash = hashString(ransomNote), hashString(magazine)

        for k in noteHash.keys():
            if k not in magHash:
                return False
            elif noteHash[k] > magHash[k]:
                return False
            else:
                noteHash[k] = 0
        
        return not any(noteHash.values())


# 别人写的。。。very pythonic
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        return all(ransomNote.count(c)<=magazine.count(c) for c in set(ransomNote))


# 11.01 复习自己写, 嗯和自己第一次写比起来代码简洁多了，n = len(ransomNote) + len(magazine), T O(n) M O(n)
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_count = Counter(ransomNote)
        magazine_count = Counter(magazine)
        res = []
        for k, v in ransom_count.items():
            res.append(v <= magazine_count[k])
        return all(res)
# 改进一下不用存res更好
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_count = Counter(ransomNote)
        magazine_count = Counter(magazine)
        for k, v in ransom_count.items():
            if v > magazine_count[k]:
                return False
        return True