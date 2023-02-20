from collections import defaultdict

# 1.27 first try，自己的思路大概写在下面，30min没写完，最后一部分感觉到可能不work就直接看答案了
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # get rid of the chars not in overlapping area between set(text1) & set(text2)
        # if not text1 or not text2, return 0
        text1, text2 = [*text1], [*text2]
        common = set(text1).intersection(set(text2))
        text1, text2 = [c for c in text1 if c in common], [c for c in text2 if c in common]
        if not text1 or not text2:
            return 0
        
        # always search shorter text's char in longer text
        short, long = text1, text2
        if len(text1) > len(text2):
            short, long = long, short
        
        # find short chars' idx in long
        char_pos = [] # [ asc sorted list storing all the idx of the char in long arr ]
        pos_dict = defaultdict(list)
        for i, lc in long:
            pos_dict[lc].append(i)
        for i in range(len(short)):
            sc = short[i]
            char_pos.update(pos_dict[sc].sorted)
        
        # now with nums arr char_pos, the problem kind of degrated to LC300 longest-increasing-subsequence？
        cur_max = [1] * len(char_pos)

        # pos of the same letter can appear multiple times in cur_max, so we need to dedupe
        # if 2 continuous nums belong to the same letter in pos_dict, then they count as 1？


# 看neetcode 2D DP正解学了一下这个matrix技巧。保留了set取overlap部分的升效方法。会比他的解跑起来TM都好一些
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # get rid of the chars not in overlapping area between set(text1) & set(text2)
        # if not text1 or not text2, return 0
        common = set(text1).intersection(set(text2))
        text1, text2 = "".join(c for c in text1 if c in common), "".join(c for c in text2 if c in common)
        if not text1 or not text2:
            return 0

        # 2D DP going from bottom right to top left
        ROWS, COLS = len(text1), len(text2)
        dp = [[0] * (COLS + 1) for _ in range(ROWS + 1)]
        for i in range(ROWS - 1, -1, -1):
            for j in range(COLS - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
        return dp[0][0]