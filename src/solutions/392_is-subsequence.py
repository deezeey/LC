# 04/08 first try自己没读懂题以为要continuous的，结果不用
def isSubsequence(s: str, t: str) -> bool:
    if len(t) < len(s):
        return False
    if not s:
        return True
    # two pointers
    s_ptr, t_ptr = 0, 0
    while t_ptr < len(t):
        while t[t_ptr] == s[s_ptr]:
            s_ptr += 1
            t_ptr += 1
            if s_ptr == len(s):
                return True
        s_ptr = 0
        t_ptr += 1
    return False

def isSubsequence(s: str, t: str) -> bool:
    if len(t) < len(s):
        return False
    if not s:
        return True
    s_ptr, t_ptr = 0, 0
    while t_ptr < len(t):
        if s_ptr < len(s) and t[t_ptr] == s[s_ptr]:
            s_ptr += 1
        t_ptr += 1
    return s_ptr == len(s)
    

def testEmpty():
    s, t = "", "asd"
    assert isSubsequence(s, t) == True

def testNormal():
    s, t = "sd", "asde"
    assert isSubsequence(s, t) == True

def testNormal2():
    s, t = "sd", "asesd"
    assert isSubsequence(s, t) == True

def testNormal3():
    s, t = "sd", "asead"
    assert isSubsequence(s, t) == True

def testEmpty2():
    s, t = "qer", ""
    assert isSubsequence(s, t) == False