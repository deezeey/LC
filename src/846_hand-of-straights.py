from typing import List
from collections import Counter
import heapq

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        count = Counter(hand)
        min_hp = list(count.keys())
        heapq.heapify(min_hp)
        while min_hp:
            start = min_hp[0]
            for n in range(start, start + groupSize):
                if not n in count:
                    return False
                count[n] -= 1
                if count[n] == 0:
                    if min_hp[0] != n:
                        return False
                    heapq.heappop(min_hp)
        return True