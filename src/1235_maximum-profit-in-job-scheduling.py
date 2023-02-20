from typing import List
import heapq

# 10.22 first try，自己想用heap做，写了俩小时跑过了12/30个case
# 碰到startTime = [1,2,2,3] endTime = [2,5,3,4] profit = [3,4,1,2] 时候挂了
# 因为（1，2）= 3这个job后面先被放上了（3，4）= 2，这样新的solution thread就不会再考虑（1，2）= 3了。但是正解是（1，2）= 3 加上 (2, 5) = 4
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        heap = [] # min heap of (-avg_profit, duration, job_index, start_time, end_time)
        min_start_time = startTime[0]
        max_end_time = endTime[0]

        # build heap
        for i in range(len(profit)):
            min_start_time, max_end_time = min(min_start_time, startTime[i]), max(max_end_time, endTime[i])
            duration = endTime[i] - startTime[i]
            avg_profit = profit[i]/duration
            heapq.heappush(heap, (-1 * avg_profit, duration, i, startTime[i], endTime[i]))

        total_time_span = max_end_time - min_start_time
        max_profit = 0
        possible_solution = {} # first_popped_job_index: max_profit or these intervals in solution
        solution_intervals = {} # first_popped_job_index:[(intervals)]

        while heap:
            cur_job = heapq.heappop(heap)
            cur_job_avg_profit = -1 * cur_job[0]
            cur_job_index, cur_job_start, cur_job_end = cur_job[2], cur_job[3], cur_job[4]
            cur_job_profit = profit[cur_job_index]

            if not max_profit:
                possible_solution[cur_job_index] = cur_job_profit
                solution_intervals[cur_job_index] = [(cur_job_start, cur_job_end)]
                max_profit += cur_job_profit
                continue

            for k, v in solution_intervals.copy().items():
                if all(end <= cur_job_start or start >= cur_job_end for start, end in v):
                # there's no overlap and we can add cur profit to cur_max of this solution
                    solution_intervals[k].append((cur_job_start, cur_job_end))
                    possible_solution[k] += cur_job_profit
                    max_profit = max(possible_solution.values())
                elif cur_job_avg_profit * total_time_span > max_profit:
                # if cur job can not fit into existing solution but still looks promising enough, we build another solution thread
                    possible_solution[cur_job_index] = cur_job_profit
                    solution_intervals[cur_job_index] = [(cur_job_start, cur_job_end)]
                    max_profit = max(possible_solution.values())
                else:
                # if given all the time it can use, current max_avg_profit won't give us higher profit
                # we know it can't be the main contributer of another possible solution
                # so we can continue
                    continue

        return max_profit


# 这题比较新neet code和九章都没有答案，找到一个DP的比较容易理解
# https://www.techiedelight.com/weighted-interval-scheduling-problem/
# 看了以上解里面的dp solution自己写出来的，这个解法非常效率了. T: O(n^2), M: O(n). 如果把helper function换成binary search那可以进一步把T提升到 nlogn
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        if len(profit) == 1:
            return profit

        jobs = zip(startTime, endTime, profit)
        jobs = sorted(jobs, key = lambda job: job[1]) # sort jobs by end_time。因为我们是从前往后iterate所以sort by end time。如果从后往前iterate就要sort by start time
        max_profit_records = [None] * len(jobs) # DP array storing maxprofit at indices

        def findLastNonConflictJob(cur_job, n):
            for i in reversed(range(n)): # going backwards according to end_time
                if jobs[i][1] <= cur_job[0]: # if a job's end_time < cur_job's start_time, return its index
                    return i
            return -1 # if no non-conflict job exists, return -1

        max_profit_records[0] = jobs[0][2]

        for i in range(1, len(jobs)):
            cur_job = jobs[i]
            cur_max_profit = cur_job[2]
            last_non_conflict_job_index = findLastNonConflictJob(cur_job, i)
            if last_non_conflict_job_index != -1: 
            # if non conflict prev job is found, max at cur index will be max at latest non conflict index + cur job profit
                cur_max_profit += max_profit_records[last_non_conflict_job_index]
                max_profit_records[i] = cur_max_profit
            # need to compare with prev max profit again
            max_profit_records[i] = max(cur_max_profit, max_profit_records[i-1])

        # print(jobs)
        # print(max_profit_records)
        return max_profit_records[len(jobs) - 1]


# leet code 官方solution 3的python版本 T O(nlogn) M O(n)
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit))
        maxprofit = 0
        heap = []
        
        for start, end, profit in jobs:
            while heap and start >= heap[0][0]:
                maxprofit = max(maxprofit, heap[0][1])
                heapq.heappop(heap)
            
            combined_job = (end, profit + maxprofit)
            
            heapq.heappush(heap, combined_job)
            
        while heap:
            maxprofit = max(maxprofit, heap[0][1])
            heapq.heappop(heap)
        
        return maxprofit


# 11.28 复习毫无思路。看了leet code官方讲解。为什么应该想到用DP。因为 1）每个当前decision是受到上一个decision影响的。 2）要求连续decision以达到某事物的最大值。
# There are two key characteristics of this problem that we should take note of at this time. 
# First, a job cannot be scheduled if a conflicting job has already been scheduled. In other words, each decision we make is affected by the previous decisions we have made. 
# Second, the problem asks us to maximize the profit by scheduling non-conflicting jobs. 
# These are two common characteristics of dynamic programming problems, and as such we will approach this problem using dynamic programming.

# 把DP解法按照从前往后iterate再写了一遍， helper function写成了binary search。这下T是nlogn了
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        if len(profit) == 1:
            return profit[0]
        
        jobs = list(zip(startTime, endTime, profit))
        jobs.sort(key = lambda x: x[0])

        max_profit_record = [0] * len(jobs)
        max_profit_record[-1] = jobs[-1][2]

        def findNextNonConflict(cur_job_idx):
            # return the index of next job with start_time >= cur_job's end_time
            cur_end_time = jobs[cur_job_idx][1]
            s, e = cur_job_idx, len(jobs) - 1
            while s <= e:
                mid = (s + e) // 2
                if jobs[mid][0] >= cur_end_time:
                    if jobs[mid - 1][0] < cur_end_time:
                        return mid
                    else:
                        e = mid - 1
                else:
                    s = mid + 1
            return -1

        for i in range(len(jobs) - 2, -1, -1):
            cur_job = jobs[i]
            cur_max_profit = cur_job[2]
            next_non_conflict = findNextNonConflict(i)
            if next_non_conflict != -1:
                cur_max_profit = cur_max_profit + max_profit_record[next_non_conflict]
            max_profit_record[i] = max(cur_max_profit, max_profit_record[i+1])
        
        return max_profit_record[0]
            