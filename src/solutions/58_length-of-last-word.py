# 04/08 first try 别看是easy，容易想不到某些edge test case
def lengthOfLastWord(s: str) -> int:
    s = s.strip()
    if not s:
        return 0
    i = len(s) - 1
    while i >= 0:
        if s[i] == " ":
            return len(s) - i - 1
        i -= 1
    return len(s) if i == -1 else 0
    

def test1():
    s = "Hello World"
    assert lengthOfLastWord(s) == 5

def test2():
    s = "Hello World   "
    assert lengthOfLastWord(s) == 5

def test3():
    s = ""
    assert lengthOfLastWord(s) == 0

def test4():
    s = " "
    assert lengthOfLastWord(s) == 0

def test5():
    s = "a"
    assert lengthOfLastWord(s) == 1