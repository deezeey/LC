from typing import List

# 12.05 第一遍没咋看懂题目这个是chatGPT的idea lol感觉基本算cheat
#  O(n) O(n)
class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encoded_string = ""
        for string in strs:
            encoded_string += str(len(string)) + ":" + string
        return encoded_string
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        decoded_list = []
        i = 0
        while i < len(s):
            len_str = ""
            while i < len(s) and s[i].isdigit():  # <-- 一开始最外层的loop不满足条件以后还会进来这里并告诉我index out of range。所以这行的i < len(s)不能省！
                len_str += s[i]
                i += 1
            str_length = int(len_str)
            if str_length:
                decoded_list.append(s[i + 1:i + 1 + str_length])
            else:
                decoded_list.append("")
            i += str_length + 1

        return decoded_list

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))


# 12.08 复习
class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + ":" + s
        return encoded

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        decoded = []
        length = 0
        i = 0

        while i < len(s):
            c = s[i]
            if c.isdigit():
                length = length * 10 + int(c)
            elif c == ":":
                decoded.append(s[i + 1: i + 1 + length])
                i = i + length
                length = 0
            else:
                raise ValueError("Encountering a string that's not digit or :")
            i += 1
        
        return decoded

# 1.2 复习
class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        res = ""
        for s in strs:
            length = len(s)
            res = res + str(length) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        i = 0
        num = ""
        res = []
        while i < len(s):
            if s[i] != "#":
                num += s[i]
            else:
                length = int(num)
                num = "" #一开始忘了reset num出了错
                res.append(s[i+1:i+length+1])
                i += length
            i += 1
        return res