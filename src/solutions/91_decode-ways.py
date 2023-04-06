
# 1.26 first try自己在30min内写出来的解能pass 230/269 cases，碰到“230"嗝屁了
class Solution:
    def numDecodings(self, s: str) -> int:
        # break s into array, if 0 appears, stick it to the end of prev num
        # array to store max ways at index, arr[0] = 1
        # if int(s[i-1] + s[i]) <= 26, arr[i] = arr[i-1] + 1 else arr[i-1]
        if s[0] == "0":
            return 0
        s_arr = [*s]
        for i in range(len(s_arr)):
            if s_arr[i] == "0":
                if s_arr[i-1] == "0":
                    return 0
                s_arr[i-1] += "0"

        s_arr = [s for s in s_arr if s != "0"]

        max_arr = [1] * len(s_arr)
        for i in range(1, len(max_arr)):
            if int(s_arr[i-1] + s_arr[i]) <= 26:
                if i > 2:
                    max_arr[i] = max_arr[i-2] + max_arr[i-1]
                else:
                    max_arr[i] = max_arr[i-1] + 1
            else:
                max_arr[i] = max_arr[i-1]

        return max_arr[-1]