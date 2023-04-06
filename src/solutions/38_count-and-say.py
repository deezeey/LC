# 不知道为什么今天状态特别不好一题都写不出来？！
class Solution:
    def __init__(self):
        self.cur = "1"

    def read(self):
        cur = self.cur
        if cur == "1":
            self.cur = "11"
            return
        count, say, res = 1, cur[0], ""
        for i in range(1, len(cur)):
            if cur[i] == say:
                count += 1
            else:
                res += (str(count) + say)
                say = cur[i]
                count = 1
        self.cur = res

    def countAndSay(self, n: int) -> str:
        for _ in range(n):
            self.read()
        return self.cur

# 改进了一下终于过了TM 还都很不错，就是太烦的时候做不了这种题哎
class Solution:
    def __init__(self):
        self.cur = "1"

    def read(self):
        cur = self.cur
        res, count, say = "", 0, ""
        for i in range(len(cur)):
            if say and cur[i] == say:
                count += 1
            else:
                if say:
                    res += (str(count) + say)
                say = cur[i]
                count = 1
        res += (str(count) + say)
        self.cur = res

    def countAndSay(self, n: int) -> str:
        for _ in range(n-1):
            self.read()
        return self.cur


# 别人写的解
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        def sayNumber(n):
            n = str(n)
            say = ""
            curDigit = n[0]
            digCount = 1
            for dig in n[1:]:
                if dig == curDigit:
                    digCount += 1
                else:
                    say += str(digCount) + curDigit
                    curDigit = dig
                    digCount = 1
            say += str(digCount) + curDigit
            return say
        
        return sayNumber(self.countAndSay(n-1))

# 官方的解
class Solution:
    def countAndSay(self, n):
        current_string = '1'
        for _ in range(n - 1):
            next_string = ''
            j = 0
            k = 0
            while j < len(current_string):
                while (k < len(current_string) and
                        current_string[k] == current_string[j]):
                    k += 1
                next_string += str(k - j) + current_string[j]
                j = k
            current_string = next_string
        return current_string