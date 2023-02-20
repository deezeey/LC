# 2.9 first try 真他娘的难写，反正我就写成这样了能过几个test case可以了，面试看到这种数学题直接放弃好了吧
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        res = ""
        seen = {} #(num, idx in res)
        nm, dnm = numerator, denominator
        while True:
            if nm == 0:
                return res
            if nm in seen:
                res = res[:seen[nm]] + "(" + res[seen[nm]:] + ")"
                return res
            if nm < dnm:
                if not res:
                    res += "0."
                else:
                    res += "0"
                nm = nm * 10
            else:
                res += str(nm // dnm)
                nm = (nm % dnm) * 10
                seen[nm] = len(res) - 1
        return res 

# 别人写的，放这儿参考一下吧
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0: return '0'
        
        result = []
        if numerator < 0 and denominator > 0 or numerator >= 0 and denominator < 0:
            result.append('-')
        
        numerator, denominator = abs(numerator), abs(denominator)
        
        result.append(str(numerator // denominator))
        
        remainder = numerator % denominator
        
        if remainder == 0: return ''.join(result)
        result.append('.')
        
        d = {}
        while remainder != 0:
            if remainder in d:
                result.insert(d[remainder], '(')
                result.append(')')
                return ''.join(result)
            
            d[remainder] = len(result)
            
            remainder *= 10
            result += str(remainder // denominator)
            remainder = remainder % denominator
        
        return ''.join(result)