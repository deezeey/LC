import heapq
from collections import deque, Counter
from typing import List

# 10. 14 first try 自己的思路是grid但是想不出来具体怎么继续了
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)

        # min_time_for_task = count(task) + n * (count(task) - 1)
        # imagine we have a grid with cols = n + 1 and rows = most_repetitive_task_count
        # every task can be filled in vertically
        # we just need to figure out how to fill in the empty cells
        # if the grid is not large enough to fill in all the tasks
        # we need to add more time to result

        task_count = {t: tasks.count(t) for t in set(tasks)}
        ordered_tasks = sorted(task_count, key=task_count.get, reverse=True)
        
        # build the grid, first col is already filled in by ordered_tasks[0] so we can ignore
        # hence cols = n, not n+1
        rows = task_count[ordered_tasks[0]]
        cols = n


# 正确答案是用max heap做，它会一直告诉你当前most frequent task是什么，maxheap是log n算法但是这个题目要iterate thru tasks to count然后要不断pop和add所以是o(n),for both T and M
        # create a max heap of tasks based on frequency
        # pop & process the most frequent task from the heap
        # calculate next time when it becomes available and add it to the waiting queue
        # if there's a task available at current time add it back to the max heap
        count = Counter(tasks)
        maxHeap = [ -freq for freq in count.values()] # heapq support min heap natively so turning everything to negative
        heapq.heapify(maxHeap)
        q = deque()
        time = 0

        while maxHeap or q:
            time += 1
            if not maxHeap:
                time = q[0][1]
            else:
                cur = heapq.heappop(maxHeap)
                cur += 1
                if cur: # <--- 不要漏掉这一句否则会stackoverflow
                    q.append([cur, time + n])  # <---这里是time + n 不是time + n + 1的原因是。
                    # 比如1的时候schedule了A, n=2, 那么A在4的时候可被re-schedule，但我们需要在3时候把它加回到max heap，而不是4。
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        
        return time
        

# 另外一个suppose to be 最efficient的解法可惜我看不懂
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d,count,l = {},0,len(tasks)
        if not n: return l
        for c in tasks:
            if c in d:
                d[c] +=1
            else:
                d[c] = 1
        max_val = max(d.values())
        for i in d.values():
            if i == max_val:
                count+=1
        return max((max_val-1)*(n+1)+count,l)


# 11.10 复习自己终于看懂了数学方法
# 假设我们的tasks是{a:3, b:3, c:2, d:1, e:2, f:1, g:3, h:3, i:3} 然后冷却时间是2
# 1）首先我们最frequent的task是a和b，各有3个，我们先取出task a，构建一个slot
# 2）a _ _ a _ _ a <--- 这个的长度是 (3 - 1) * 2 + 3 很好理解
# 3）然后我们知道如果把b放进去变成 a b _ a b _ a [b] 是要在原长度基础上加一个[b], 这是count_of_longest - 1, 加在原来的长度上面
# 4）我们有 g h i 另外3个都是长度为3也没关系, 我们直接把空白slot撑爆拉长，变成 a _ _ _ _ a _ _ _ _ a [bghi] 就可以。因为slot最小是2满足冷却条件，不管把它撑多长都不违反冷却条件。
#    但是从这开始，3）得出的结论就不是最小值了，而会是total len(tasks), 所以结果需要比较 3）的结果和len(tasks)取max。至于为什么是len(tasks)下面解释。
# 5) 然后其他count更低的我们也都可以继续拉长slot插进去，因为slot变成，间隔只会更大而不会变小，所以这些task之间也不会存在冷却问题。
# a b g h i | a b g h i | a b g h i -----> a b g h i [c] [e] [d] [f] | a b g h i [c] [e] | a b g h i <---- 你看这样插完是不是 min time needed = len(tasks)？
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tasks_nums = list(Counter(tasks).values())
        longest = max(tasks_nums)
        count_of_longest = tasks_nums.count(longest)
        least_time_needed = (longest - 1) * n + longest + count_of_longest - 1
        return max(least_time_needed, len(tasks))


# 11.10 复习看了neet code代码自己重新默一遍 max heap + priority queue的解决方案
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # edge case
        if n == 0:
            return len(tasks)

        # max heap + queue
        task_count = Counter(tasks)
        max_heap = [-val for val in task_count.values()]
        heapq.heapify(max_heap)

        q = deque()
        cur_time = 0

        while max_heap or q:  # <--- 这个部分感觉neet code写的更好，尤其是如果没有maxheap time直接跳到queue第一位的时间
            cur_time += 1
            while q and q[0][0] == cur_time:
                _, available_task = q.popleft()
                heapq.heappush(max_heap, available_task)
            if max_heap:
                cur_task = heapq.heappop(max_heap)
                cur_task += 1
                if cur_task:
                    q.append((cur_time + n + 1, cur_task))

        return cur_time

# 12.11 复习自己记得数学解法
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)

        count = Counter(tasks)
        max_task = max(count.values())
        max_task_count = 0
        for k, v in count.items():
            if v == max_task:
                max_task_count += 1
        save = n + 1 - max_task_count if max_task_count <= n else 0
        res = (n + 1) * max_task - save
        return max(res, len(tasks))

# 1.9 复习自己记得数学解法，heap + priority queue的办法不记得怎么写了，看了以后又背了一遍
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        freq = list(count.values())
        max_freq = max(freq)
        max_freq_count = freq.count(max_freq)

        res = max(max_freq_count, n + 1) * max_freq - max(0, n + 1 - max_freq_count)
        return max(len(tasks), res)

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        max_hp = [-freq for freq in count.values()] #[-freq]
        heapq.heapify(max_hp)
        q = deque() #[[-freq, available_time]]
        time = 0

        while q or max_hp:
            time += 1
            if not max_hp:
                time = q[0][1]
            else:
                cur = heapq.heappop(max_hp)
                cur += 1
                if cur:
                    q.append([cur, time + n])
            if q and q[0][1] == time:
                freq, _ = q.popleft()
                heapq.heappush(max_hp, freq)
        
        return time