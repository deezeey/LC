# 2.8 first try brute force way。没啥用早就知道会TLE了
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0

        sign = -1
        if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0):
            sign = 1
        
        dividend, divisor = abs(dividend), abs(divisor)
        cur, cnt = 0, 0
        
        while cur < dividend:
            cur += divisor
            cnt += 1
        
        if cur == dividend:
            return cnt if sign > 0 else -cnt
        if cur > dividend:
            return cnt - 1 if sign > 0 else -(cnt - 1)

# exponential search勉强算是个能过面试的算法吧
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0

        sign = -1
        if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0):
            sign = 1
        
        dividend, divisor = abs(dividend), abs(divisor)
        power_arr = [[divisor, 1]] #[num, power]
        cur_num, cur_power, cur_res = divisor, 1, 0
        while cur_res < dividend:
            cur_res = cur_num + cur_num
            cur_power = cur_power + cur_power
            cur_num = cur_res
            power_arr.append([cur_res, cur_power])
        # dividend : 60, dividsor: 3 will give
        # [[3, 1], [6, 2], [12, 4], [24, 8], [48, 16], [96, 32]]
        print(power_arr)
        res_cnt = 0
        for i in range(len(power_arr) - 1, -1, -1):
            num, cnt = power_arr[i]
            if num > dividend:
                continue
            res_cnt += cnt
            dividend -= num
            if dividend <= 0 or i == 0:
                break
        res_cnt = min(res_cnt, 2**31 - 1) if sign > 0 else max(-res_cnt, - 2**31)
        return res_cnt