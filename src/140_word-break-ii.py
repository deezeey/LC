from typing import List
from collections import Counter, defaultdict
# 第一次自己做出来hard DP problem虽然花了很多时间，但是还是觉得自己很棒？
class trieNode:
    def __init__(self, val=""):
        self.val = val
        self.end = False
        self.children = {}

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        trie = trieNode()
        # build trie
        for w in wordDict:
            cur = trie
            for c in w:
                if c not in cur.children:
                    node = trieNode(c)
                    cur.children[c] = node
                cur = cur.children[c]
            cur.end = True
            # print(cur.val, cur.end)
        
        # initiate dp arr
        dp = [False] * len(s) # ex: [(3,4), F, F, 7, 7, F, F, 10, F, F] which means, 0-2, 0-3, 3-6, 4-6, 7-9 can form words
        # iterate thru the string backwards to fill in dp arr
        i = len(s) - 1
        while i >= 0 :
            # if s[i] in trie, start to look for a word
            if s[i] in trie.children:
                j = i
                cur = trie
                # continue traversing the trie until out of bounds or char not in trie
                while j < len(s) and s[j] in cur.children:
                    # if we see an end of word, check if j + 1 == len(s) or dp[j + 1] is not False, if so, add j + 1 to dp
                    if cur.children[s[j]].end and (j + 1 == len(s) or dp[j + 1]):
                        if not dp[i]:
                            dp[i] = {j + 1}
                        else:
                            dp[i].add(j + 1)
                    cur = cur.children[s[j]]
                    j += 1
            i -= 1

        res = []
        # iterate thru the dp to form a result
        def formPath(k, path):
            print(k)
            if k < len(s) and not dp[k]:
                return
            new_path = path + [k]
            if k == len(s):
                res.append(pathToStr(new_path))
                return
            for next_k in dp[k]:
                formPath(next_k, new_path)
                
        def pathToStr(path):
            # (0, 3, 7, 10)
            idx, str_arr = 0, []
            while idx < len(path) - 1:
                b, e = path[idx], path[idx + 1]
                str_arr.append(s[b:e])
                idx += 1
            return " ".join(str_arr)

        formPath(0, [])
        return res
    
# 官方top down DP，DFS, 也类似backtracking的思路
# Let N be the length of the input string and W be the number of words in the dictionary.
# T O(N^2 + 2^N + W) M O(2^N * N + W) 
# worst case 比如 s = "aaa", wordDict = ["a", "aa", "aaa"] 有N种postfix，每个postfix我们是一个一个字母invocate的，所以就是等差数列1-N求和 = (1+N)N / 2即N^2
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)
        # table to map a string to its corresponding words break
        # {string: [['word1', 'word2'...], ['word3', 'word4', ...]]}
        memo = defaultdict(list)  # O(W)

        #@lru_cache(maxsize=None)    # alternative memoization solution
        def _wordBreak_topdown(s):
            """ return list of word lists """
            if not s:
                return [[]]  # list of empty list

            if s in memo:
                # returned the cached solution directly.
                return memo[s]

            for endIndex in range(1, len(s)+1):
                word = s[:endIndex]
                if word in wordSet:
                    # move forwards to break the postfix into words
                    for subsentence in _wordBreak_topdown(s[endIndex:]):
                        # 这个for loop是保证如果剩下的str没有可用的解那么memo[s]也会是空集的
                        memo[s].append([word] + subsentence)
            return memo[s]

        # break the input string into lists of words list
        _wordBreak_topdown(s) # worst case O(N^2) edges

        # chain up the lists of words into sentences.
        return [" ".join(words) for words in memo[s]] # O(2^N), worst case dp里有N个postfix，每个长度为i的postfix可以有2^(i-1)个解
    
# 官方bottom up DP, BFS, worse performance then previous DFS b/c it keeps intermediate solutions
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # quick check on the characters,
        # otherwise it would exceed the time limit for certain test cases.
        # check if there's any letter in s not in wordDict words
        if set(Counter(s).keys()) > set(Counter("".join(wordDict)).keys()):
            return []

        wordSet = set(wordDict)

        dp = [[]] * (len(s)+1)
        dp[0] = [""]

        for endIndex in range(1, len(s)+1):
            sublist = []
            # fill up the values in the dp array.
            for startIndex in range(0, endIndex):
                word = s[startIndex:endIndex]
                if word in wordSet:
                    for subsentence in dp[startIndex]:
                        sublist.append((subsentence + ' ' + word).strip())

            dp[endIndex] = sublist

        return dp[len(s)]

# 自己重写了一遍DFS
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)
        dp = defaultdict(list) # {'string':[[word combo1], [word combo2]]}

        def _breakString(s):
            if not s:
                return [[]]  #这里注意一定是[[]]而不能写[]
            if s in dp:
                return dp[s]
            for i in range(1, len(s) + 1):
                cur_str = s[:i]
                if cur_str in wordSet:
                    for combo in _breakString(s[i:]):
                        dp[s].append([cur_str] + combo)
            return dp[s]
        
        _breakString(s)
        return [" ".join(combo) for combo in dp[s]]