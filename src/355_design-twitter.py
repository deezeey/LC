from collections import defaultdict
from typing import List
import heapq

# 12.11 first try自己写出来了
class Twitter:

    def __init__(self):
        self.time = 0
        self.following = defaultdict(set)
        self.user_post = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.follow(userId, userId)
        self.user_post[userId].add((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        max_heap = []
        for followee in self.following[userId]:
            max_heap.extend(self.user_post[followee])
        max_heap = [(-t, idx) for t, idx in max_heap]
        heapq.heapify(max_heap)
        res = []
        for _ in range(10):
            if max_heap:
                res.append(heapq.heappop(max_heap)[1])
        return res
        
    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)

# neetcode解法，相当于它的time就是负数记的，这样直接可以用minheap了
# 还有就是它不是直接extend全部followee的tweets而是从最后一个开始一批一批的push这样很节省流量
class Twitter:
    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list)  # userId -> list of [count, tweetIds]
        self.followMap = defaultdict(set)  # userId -> set of followeeId

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []

        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1
                # 他只push最后一条tweet到minheap，push的不只有tweet id还有一堆别的东西，最重要的，下一个idx
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])

        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)

# 1.4复习也用了一批一批push到heap的方法。
# 注意定义的attribute不要和method同名。一开始我定义的self.follow hashmap和follow method重名了找了半天问题。
class Twitter:

    def __init__(self):
        self.followmap = defaultdict(set)
        self.tweet = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet[userId].append([self.time, tweetId])
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        followees = self.followmap[userId]
        followees.add(userId)
        batch, res = [], []

        for followee in followees:
            if followee in self.tweet:
                idx = len(self.tweet[followee]) - 1 # id of the last tweet
                time, tId = self.tweet[followee][idx]
                batch.append([time, tId, followee, idx - 1]) # idx - 1 gives us access the the next most recent tweet
        heapq.heapify(batch)

        while batch and len(res) < 10:
            time, tId, followee, idx = heapq.heappop(batch)
            res.append([time, tId])
            if idx >= 0:
            # 如果这个用户还有下一条tweet，把它也push到min heap里
                time, tId = self.tweet[followee][idx]
                heapq.heappush(batch, [time, tId, followee, idx - 1])
        res.sort() #这个其实没有必要，因为假设第一条latest append到res之后，如果下一条比batch里其他的时间也要晚，
        # 它被push进去之后自然会成为while loop的第二个iteration
        # 这种自带下一条idx指针的方法能够保证我们每次下一个iteration都是latest atm
        return [t[1] for t in res]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followmap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followmap[followerId]:
            self.followmap[followerId].remove(followeeId)

# 1.9 复习想了一阵子还是没记起那个只get 10条tweets的方法的细节 ，看了答案又默了一遍
class Twitter:

    def __init__(self):
        self.following = defaultdict(set)
        self.tweets = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time -= 1
        self.tweets[userId].append([self.time, tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        if not userId in self.following:
            self.following[userId].add(userId)

        hp = []
        for f in self.following[userId]:
        # getting last tweets of every followee and push to heap
            if f in self.tweets:
                idx = len(self.tweets[f]) - 1
                time, tId = self.tweets[f][idx]
                hp.append([time, tId, f, idx - 1])
        heapq.heapify(hp)

        while hp and len(res) < 10:
            time, tId, f, idx = heapq.heappop(hp)
            res.append(tId)
            if idx >= 0:
                time, tId = self.tweets[f][idx]
                heapq.heappush(hp, [time, tId, f, idx - 1])
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followerId)
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following:
            self.following[followerId].remove(followeeId)