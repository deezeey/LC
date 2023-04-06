from collections import Counter

# 12.14 first try 这个碰到s1 = "adc" s2 = "dcda"时候挂了
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool: 
        cur_count = Counter(s1)
        cur_total = len(s1)
        l, r = 0, 0
        while r < len(s2):
            if s2[r] not in cur_count or cur_count[s2[r]] == 0:
                l, r = r + 1, r + 1
                cur_count = Counter(s1)
                cur_total = len(s1)
            else:
                cur_count[s2[r]] -= 1
                cur_total -= 1
                if cur_total == 0:
                    return True
                r += 1
        
        return False


# 固定长度滑动窗口，偷懒用counter的写法
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool: 
        count = Counter(s1)
        LEN = len(s1)
        l, r = 0, LEN

        while r <= len(s2):
            cur = Counter(s2[l:r])
            if cur == count:
                return True
            else:
                l += 1
                r += 1
        
        return False

# 另一个写法
class Solution:
    def checkInclusion(self, s1, s2):
        l1 = len(s1)
        need = Counter(s1) # letter needed can be negative!
        missing = l1
        for i,c in enumerate(s2):
            if c in need: 
                if need[c] > 0: missing -= 1    
                need[c] -= 1                    
            if i>=l1 and s2[i-l1] in need:      
                need[s2[i-l1]] += 1            
                if need[s2[i-l1]]>0: missing += 1  
                #为什么这里需要条件句，就看"adc" in "dcda"这个例子，当超出窗口长度s2[i-l1]这时候是第一个"d",而这个need["d"]在+1以后还是=0，因为之前它是-1
            if missing == 0:
                return True
        return False

# 自己默写了一遍
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = Counter(s1)
        LEN = len(s1)
        missing = LEN

        for i, c in enumerate(s2):
            if c in need:
                need[c] -= 1
                if need[c] >= 0:
                    missing -= 1
            if i >= LEN and s2[i-LEN] in need:
                need[s2[i-LEN]] += 1
                if need[s2[i-LEN]] > 0:
                    missing += 1
            if not missing:
                return True
        
        return False

# 1.5 自己写了一下，写的好复杂，看上面代码根本用不着l,r两个pointer，一个i然后当超出string长度特殊处理就是了
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        need = len(s1)
        count = Counter(s1)
        l, r = 0, len(s1) - 1

        for i in range(r + 1):
            c = s2[i]
            if c in count:
                count[c] -= 1
                if count[c] >= 0:
                    need -= 1
            if need == 0:
                return True

        while r < len(s2) - 1:
            l_c = s2[l]
            if l_c in count:
                count[l_c] += 1
                if count[l_c] > 0:
                    need += 1
            l += 1
            r += 1
            r_c = s2[r]
            if r_c in count:
                count[r_c] -= 1
                if count[r_c] >= 0:
                    need -= 1
            if need == 0:
                return True
        
        return False