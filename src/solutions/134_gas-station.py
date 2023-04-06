from typing import List

# 1.31 first try，一开始30min没想通，结果吃完午饭回来做出来了， O(n)
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        remain = [0] * len(gas)
        for i in range(len(gas)):
            remain[i] = gas[i] - cost[i]
        
        cur = 0
        i, start = 0, 0
        while i < len(remain):
            cur += remain[i]
            if cur < 0:
                cur = 0
                start = i + 1
            i += 1
        return start if cur + sum(remain[:start]) >= 0 else -1