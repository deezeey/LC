from typing import List
import random

# 2.24 first try感觉自己写的没错但是仍然过不了test case，看result是totally valid的
# 可能init里面必须要有一个arr吧
class Solution:

    def __init__(self, nums: List[int]):
        self.original_hash = {} # orig_idx: orig_val
        self.n = len(nums)
        for i, v in enumerate(nums):
            self.original_hash[i] = v
        
    def reset(self) -> List[int]:
        res = [0] * self.n
        for k, v in self.original_hash.items():
            res[k] = v
        return res

    def shuffle(self) -> List[int]:
        idx_arr = [idx for idx in range(self.n)]
        for i in range(self.n - 1):
            target = i
            while target == i:
                target = random.choice(idx_arr)
            idx_arr[i], idx_arr[target] = idx_arr[target], idx_arr[i] #[0 ~ 1] or [0 ~ 2]
        return [self.original_hash[j] for j in idx_arr]
    

# 官方的解就是用arr。reset function的deep copy要注意一下，直接return self.orig_arr可以过，但是题目明确要求更改原arr并且return它
# 所以必须变更self.arr，
class Solution:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.arr = nums
        self.orig_arr = nums[::]
        
    def reset(self) -> List[int]:
        self.arr = self.orig_arr
        self.orig_arr = self.orig_arr[::]  
        # 注意为什么需要这行，因为上面我们已经把 self.arr和self.orig_arr point到了同一份data，
        # 那么下一次shuffle，你变更self.arr时候也就等于shuffle了orig_arr。所以要重新create deep copy for orig_arr
        return self.arr

    def shuffle(self) -> List[int]:
        for i in range(self.n):
            target = random.randrange(i, self.n)
            self.arr[i], self.arr[target] = self.arr[target], self.arr[i]
        return self.arr