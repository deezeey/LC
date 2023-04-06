from typing import List
# 2.27 first try没有想好existInorder如何handle ？。比如 "cdebbac" 如何和 "*b?c" match 上
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # move i and j when c matches or "?" in p
        # after first "*", check substring after it after deleting the "*"s, if all the chars & "?" in it exist in order in s[i:]
        i, j = 0, 0
        while i < len(s) and j < len(p):
            while s[i] == p[j] or p[j] == "?":
                i += 1
                j += 1
            if s[i] != p[j] and p[j] != "*":
                return False
            else:
                return self.existInOrder(s[i:], p[j:])
    def existInOrder(s: List, p: List) -> bool:
        while i < len(s) and j < len(p):
            while p[j] == "*":
                j += 1
            p_c = p[j]
            while s[i] != p_c:
                i += 1
            i += 1
            j += 1

# 看了2D DP的解释自己写的. 具体看图。 居然TLE。。
# instantiate一个2D matrix.
# 如果当前字母match或p是?，那么如果前一位match(cell[r-1][c-1] val 是True)的话，本位res也是match。
# 如果当前p是*，那么如果前一位match,那么当前*的这一行或一列（取决于p放在行还是列）就会match从此以后的所有行或列（取决于s放在行或列）
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # handle edge case
        if not s:
            return all(c == "*" for c in p)
        # get rid of duplicated "*"s
        new_p = ""
        for i in range(len(p)):
            c = p[i]
            if c == "*":
                if i >= 1 and p[i-1] == "*":
                    continue
            new_p += c
        p = new_p

        # instantiate 2D matrix
        ROWS, COLS = len(p) + 1, len(s) + 1
        dp = [[False] * COLS for _ in range(ROWS)]
        dp[0][0] = True
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if dp[r][c]:
                    continue
                prev_r, prev_c = r - 1, c - 1
                if prev_r >= 0 and prev_c >= 0: 
                    if p[r - 1] == s[c - 1] or p[r - 1] == "?":
                        dp[r][c] = dp[prev_r][prev_c]
                    elif p[r - 1] == "*":
                        for new_c in range(COLS):
                            # this "*" can match any sequence or matches ""
                            matches_many = True if new_c > prev_c and dp[prev_r][prev_c] else False 
                            matches_none = True if dp[r - 1][new_c] else False # 这里很容易漏掉matches none的情况
                            dp[r][new_c] = matches_many or matches_none
                    else:
                        continue
        return dp[ROWS - 1][COLS - 1]

# 官方的2D DP能过还beat 70%？
# 2D DP TM 都是len(s) * len(p)
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_len = len(s)
        p_len = len(p)
        
        # base cases
        if p == s or set(p) == {'*'}:
            return True
        if p == '' or s == '':
            return False
        
        # init all matrix except [0][0] element as False
        d = [[False] * (s_len + 1) for _ in range(p_len + 1)]
        d[0][0] = True
        
        # DP compute 
        for p_idx in range(1, p_len + 1):
            # the current character in the pattern is '*'
            if p[p_idx - 1] == '*':
                s_idx = 1
                                        
                # d[p_idx - 1][s_idx - 1] is a string-pattern match 
                # on the previous step, i.e. one character before.
                # Find the first idx in string with the previous math.
                while not d[p_idx - 1][s_idx - 1] and s_idx < s_len + 1:
                    s_idx += 1
    
                # If (string) matches (pattern), 
                # when (string) matches (pattern)* as well
                d[p_idx][s_idx - 1] = d[p_idx - 1][s_idx - 1]
    
                # If (string) matches (pattern), 
                # when (string)(whatever_characters) matches (pattern)* as well
                while s_idx < s_len + 1:
                    d[p_idx][s_idx] = True
                    s_idx += 1
                                   
            # the current character in the pattern is '?'
            elif p[p_idx - 1] == '?':
                for s_idx in range(1, s_len + 1): 
                    d[p_idx][s_idx] = d[p_idx - 1][s_idx - 1] 
                                   
            # the current character in the pattern is not '*' or '?'
            else:
                for s_idx in range(1, s_len + 1): 
                    # Match is possible if there is a previous match
                    # and current characters are the same
                    d[p_idx][s_idx] = d[p_idx - 1][s_idx - 1] and p[p_idx - 1] == s[s_idx - 1]  
                                                               
        return d[p_len][s_len]

# 把自己的改了一下能过了
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # handle edge case
        if not s:
            return all(c == "*" for c in p)
        # get rid of duplicated "*"s
        new_p = ""
        for i in range(len(p)):
            c = p[i]
            if c == "*":
                if i >= 1 and p[i-1] == "*":
                    continue
            new_p += c
        p = new_p

        # instantiate 2D matrix
        ROWS, COLS = len(p) + 1, len(s) + 1
        dp = [[False] * COLS for _ in range(ROWS)]
        dp[0][0] = True
        for r in range(1, ROWS):
            if p[r - 1] == "*":
                c = 0
                while c < COLS and not dp[r - 1][c]: #find first match of s using prev pattern
                    c += 1
                while c < COLS: # cell under it and all the cells to its right should be True
                    dp[r][c] = True
                    c += 1
            else:
                for c in range(1, COLS):
                    if (p[r - 1] == s[c - 1] or p[r - 1] == "?") and dp[r - 1][c - 1]:
                        dp[r][c] = True
                
        return dp[ROWS - 1][COLS - 1]


# backtracking
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_len, p_len = len(s), len(p)
        s_idx = p_idx = 0
        star_idx = s_tmp_idx = -1
 
        while s_idx < s_len:
            # If the pattern caracter = string character
            # or pattern character = '?'
            if p_idx < p_len and p[p_idx] in ['?', s[s_idx]]:
                s_idx += 1
                p_idx += 1
    
            # If pattern character = '*'
            elif p_idx < p_len and p[p_idx] == '*':
                # Check the situation
                # when '*' matches no characters
                star_idx = p_idx
                s_tmp_idx = s_idx
                p_idx += 1
                              
            # If pattern character != string character
            # or pattern is used up
            # and there was no '*' character in pattern 
            elif star_idx == -1:
                return False
                              
            # If pattern character != string character
            # or pattern is used up
            # and there was '*' character in pattern before
            else:
                # Backtrack: check the situation
                # when '*' matches one more character
                p_idx = star_idx + 1
                s_idx = s_tmp_idx + 1
                s_tmp_idx = s_idx
        
        # The remaining characters in the pattern should all be '*' characters
        return all(p[i] == '*' for i in range(p_idx, p_len))
    

# 自己写一遍backtracking过不了s = "aa" p = "*"的case
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # handle edge case
        if not s:
            return all(c == "*" for c in p)
        # get rid of duplicated "*"s
        new_p = ""
        for i in range(len(p)):
            c = p[i]
            if c == "*":
                if i >= 1 and p[i-1] == "*":
                    continue
            new_p += c
        p = new_p

        # backtracking
        s_idx, p_idx = 0, 0
        star_idx, post_star_s_idx = -1, -1
        while s_idx < len(s) and p_idx < len(p): #这里不能限制p_idx要within bound
            if s[s_idx] == p[p_idx] or p[p_idx] == "?":
                # same char or pattern is "?", move both pointers
                s_idx += 1
                p_idx += 1
            elif p[p_idx] == "*":
                # pattern is "*", try treating it as empty string first
                star_idx = p_idx
                post_star_s_idx = s_idx
                p_idx += 1
            elif star_idx == -1:
                # if we encounter 2 diff chars and we haven't seen a star before
                return False
            else:
                # if we encounter 2 diff chars and we have a star before, backtrack and see if adding one more char from s to "*" mapping would help
                p_idx = star_idx + 1
                post_star_s_idx = post_star_s_idx + 1
                s_idx = post_star_s_idx
        return s_idx >= len(s) and (p_idx >= len(p) or all(c == "*" for c in p[p_idx:]))
    
# 改了一下过不了"aaaa"和"***a"的case。"*a"会run out, s还剩"aaa"没有match，我们需要重新考虑* map到"a", "aa", "aaa"的情况才能得出正确结论，所以这就是while loop不能限制p要within bound的原因
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # handle edge case
        if not s:
            return all(c == "*" for c in p)
        # get rid of duplicated "*"s
        new_p = ""
        for i in range(len(p)):
            c = p[i]
            if c == "*":
                if i >= 1 and p[i-1] == "*":
                    continue
            new_p += c
        p = new_p

        # backtracking
        s_idx, p_idx = 0, 0
        star_idx, post_star_s_idx = -1, -1
        while s_idx < len(s) and p_idx < len(p):
            if s[s_idx] == p[p_idx] or p[p_idx] == "?":
                # same char or pattern is "?", move both pointers
                s_idx += 1
                p_idx += 1
            elif p[p_idx] == "*":
                # pattern is "*", try treating it as empty string first
                star_idx = p_idx
                post_star_s_idx = s_idx
                p_idx += 1
            elif star_idx == -1:
                # if we encounter 2 diff chars and we haven't seen a star before
                return False
            else:
                # if we encounter 2 diff chars and we have a star before, backtrack and see if adding one more char from s to "*" mapping would help
                p_idx = star_idx + 1
                post_star_s_idx = post_star_s_idx + 1
                s_idx = post_star_s_idx
        return (s_idx >= len(s) and p_idx >= len(p) or
                # either running out of both s and p
                s_idx <= len(s) - 1 and p[-1] == "*" or 
                # or there're still s left but we have a * at the end of p
                p_idx <= len(p) - 1 and all(c == "*" for c in p[p_idx:]))
                # or there're still p left but they'er all "*"s

# 最后一遍过了TM非常好
# T的话best case是O(min(S,P)), avg case O(SlogP), worst case(S*P)
# worst case就是每次都在最后一个不符合，然后需要backtrack entire S string every time
# 比如 s = "rrrrrrrf" p = "*rrrr"
# M是O(1)
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # handle edge case
        if not s:
            return all(c == "*" for c in p)
        # get rid of duplicated "*"s
        new_p = ""
        for i in range(len(p)):
            c = p[i]
            if c == "*":
                if i >= 1 and p[i-1] == "*":
                    continue
            new_p += c
        p = new_p

        # backtracking
        s_idx, p_idx = 0, 0
        star_idx, post_star_s_idx = -1, -1
        while s_idx < len(s):
            if p_idx < len(p) and (s[s_idx] == p[p_idx] or p[p_idx] == "?"):
                # same char or pattern is "?", move both pointers
                s_idx += 1
                p_idx += 1
            elif p_idx < len(p) and p[p_idx] == "*":
                # pattern is "*", try treating it as empty string first
                star_idx = p_idx
                post_star_s_idx = s_idx
                p_idx += 1
            elif star_idx == -1:
                # if we encounter 2 diff chars and we haven't seen a star before
                return False
            else:
                # if we encounter 2 diff chars and we have a star before, backtrack and see if adding one more char from s to "*" mapping would help
                p_idx = star_idx + 1
                post_star_s_idx = post_star_s_idx + 1
                s_idx = post_star_s_idx
        return all(c == "*" for c in p[p_idx:])