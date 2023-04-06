import heapq

# 10.19 first try自己把问题想的太简单，只pass了test case但是碰到code下面那个case就报错了
# 不能只记住中间两个数，因为如果不停往最右端加，2个pointer都要一直往右移所以还是得maintain整个数列
class MedianFinder:

    def __init__(self):
        self.count = 0
        self.middle_left = None
        self.middle_right = None
        self.median = None

    def addNum(self, num: int) -> None:
        self.count += 1
        # add first element
        if self.count == 1:
            self.middle_left = self.middle_right = self.median = num
        # add second element
        elif self.count == 2:
            if num > self.middle_left:
                self.middle_right = num
            else:
                self.middle_left = num
            self.median = (self.middle_left + self.middle_right) / 2
        # add more than second element
        else:
            if self.count % 2 == 0:
                if num > self.median:
                    self.middle_left = self.median
                    self.middle_right = min(num, self.middle_right)
                else:
                    self.middle_right = self.median
                    self.middle_left = max(num, self.middle_left)
                self.median = (self.middle_left + self.middle_right) / 2
                print(self.count, self.middle_left, self.middle_right, self.median)
            else:
                if num < self.middle_left:
                    temp = self.middle_left
                    self.middle_left = num
                    self.median = temp
                elif num > self.middle_right:
                    temp = self.middle_right
                    self.middle_right = num
                    self.median = temp
                else:
                    self.median = num
                print(self.count, self.middle_left, self.middle_right, self.median)
        
    def findMedian(self) -> float:
        return self.median

# 以下是func/input/output/expected
# ["MedianFinder","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian"]
# [[]            ,[1]     ,[]          ,[2]     ,[]          ,[3]     ,[]          ,[4]     ,[]          ,[5]     ,[]          ,[6]     ,[]          ,[7]     ,[]          ,[8]     ,[]          ,[9]     ,[]          ,[10]    ,[]]
# [null          ,null    ,1.00000     ,null    ,1.50000     ,null    ,2.00000     ,null    ,2.50000     ,null    ,3.00000     ,null    ,3.50000     ,null    ,4.00000     ,null    ,4.50000     ,null    ,5.00000     ,null    ,5.50000]
# [null          ,null    ,1.00000     ,null    ,1.50000     ,null    ,2.00000     ,null    ,2.50000     ,null    ,3.00000     ,null    ,4.00000     ,null    ,5.00000     ,null    ,6.00000     ,null    ,7.00000     ,null    ,8.00000]


# 看了neet code讲解以后知道要用heap来做，自己写的，很容易粗心大意漏掉sign change，改了一阵子终于过了，但是感觉自己写的还是稍显复杂
class MedianFinder:

    def __init__(self):
        self.left_max_heap, self.right_min_heap = [], []
        self.left_size, self.right_size = 0, 0

    def addNum(self, num: int) -> None:
        # print('add num:', num)
        # first add, add to left_max_heap, remember change the sign!
        if not self.left_size:
            heapq.heappush(self.left_max_heap, -1 * num)
            self.left_size += 1
            return

        # second add, compare to left_max and decide where to go
        if self.left_size and not self.right_size:
            if -1 * self.left_max_heap[0] > num:
                temp = -1 * heapq.heappop(self.left_max_heap)
                heapq.heappush(self.right_min_heap, temp)
                heapq.heappush(self.left_max_heap, -1 * num)
            else:
                heapq.heappush(self.right_min_heap, num)
            self.right_size += 1
            return

        # from third, compare with left_max and right_min and throw to correct heap
        # check if heap sizes are within +- 1 diff, if not need to pop from the bigger heap to smaller heap
        if num > self.right_min_heap[0]:
            heapq.heappush(self.right_min_heap, num)
            self.right_size += 1
        elif num < -1 * self.left_max_heap[0]:
            heapq.heappush(self.left_max_heap, -1 * num)
            self.left_size += 1
        else:
            if self.left_size > self.right_size:
                heapq.heappush(self.right_min_heap, num)
                self.right_size += 1
            else:
                heapq.heappush(self.left_max_heap, -1 * num)
                self.left_size += 1
        
        if self.left_size - self.right_size > 1:
            temp = -1 * heapq.heappop(self.left_max_heap)
            self.left_size -= 1
            heapq.heappush(self.right_min_heap, temp)
            self.right_size += 1
        elif self.right_size - self.left_size > 1:
            temp = heapq.heappop(self.right_min_heap)
            self.right_size -= 1
            heapq.heappush(self.left_max_heap, -1 * temp)
            self.left_size += 1
        # print(
        # 'sizes:', self.left_size, self.right_size,
        # "heaps:", list(self.left_max_heap), list(self.right_min_heap),
        # )

    def findMedian(self) -> float:
        # print(
        #     ":::find median:::",
        #     'sizes:', self.left_size, self.right_size,
        #     "heaps:", list(self.left_max_heap), list(self.right_min_heap)
        #     )
        if self.left_size == self.right_size:
            return (-1 * self.left_max_heap[0] + self.right_min_heap[0]) / 2
        elif self.left_size > self.right_size:
            return -1 * self.left_max_heap[0]
        else:
            return self.right_min_heap[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


# neet code写的非常简洁
# 首先他没有用size vars。我以为用size var可以省时间，但是其实不用，python len() func的time complexity是O(1)
# 其次他默认先全部push到左边heap，再比较两个heap的len调整，比我就省了很多if else statement
class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        # two heaps, large, small, minheap, maxheap
        # heaps should be equal size
        self.small, self.large = [], []  # maxHeap, minHeap (python default)

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num)

        if self.small and self.large and (-1 * self.small[0]) > self.large[0]:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        return (-1 * self.small[0] + self.large[0]) / 2


# 11.10 复习，自己一开始压根儿不记得要用一个minheap加一个maxheap来做，大概看了下思路自己写的
class MedianFinder:

    def __init__(self):
        self.leftMaxHeap = []
        self.rightMinHeap = []
        self.median = None

    def addNum(self, num: int) -> None:
        heapq.heappush(self.leftMaxHeap, -num)
        heapSizeDiff = len(self.leftMaxHeap) - len(self.rightMinHeap)
        if heapSizeDiff == 2:
            leftMax = -1 * heapq.heappop(self.leftMaxHeap)
            heapq.heappush(self.rightMinHeap, leftMax)
            self.median = (-1 * self.leftMaxHeap[0] + self.rightMinHeap[0]) / 2
        else:
            # heapSizeDiff == 1:
            if self.rightMinHeap:
                rightMin = self.rightMinHeap[0]
                leftMax = -1 * self.leftMaxHeap[0]
                if rightMin < leftMax:
                    heapq.heappushpop(self.rightMinHeap, leftMax)
                    heapq.heappushpop(self.leftMaxHeap, -1 * rightMin)
            self.median = -1 * self.leftMaxHeap[0]

    def findMedian(self) -> float:
        return self.median


# 12.12 复习自己记得思路了
class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        #  by default we push to min_heap (right half)
        heapq.heappush(self.min_heap, num)
        #  need to check if we need to swap the root of two heaps
        if self.max_heap and (-1 * self.max_heap[0] > self.min_heap[0]):
            min_heap_top = heapq.heappop(self.min_heap)
            max_heap_top = -1 * heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, max_heap_top)
            heapq.heappush(self.max_heap, -1 * min_heap_top)
        if len(self.min_heap) - len(self.max_heap) > 1:
            min_heap_top = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -1 * min_heap_top)

    def findMedian(self) -> float:
        if len(self.min_heap) == len(self.max_heap):
            return (self.min_heap[0] + (-1 * self.max_heap[0])) / 2
        else:
            return self.min_heap[0]