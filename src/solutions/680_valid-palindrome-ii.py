def validPalindrome(s: str) -> bool:
    if not s or len(s) == 1:
        return True
    
    def checkPalindrome(s: str, i: int, j: int) -> bool:
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
    
    i, j = 0, len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return checkPalindrome(s, i, j - 1) or checkPalindrome(s, i + 1, j)
        i += 1
        j -= 1
        
    return True


def test1():
    s = "abca"
    assert validPalindrome(s) == True

def test2():
    s = ""
    assert validPalindrome(s) == True

def test3():
    s = "aba"
    assert validPalindrome(s) == True

def test4():
    s = "abab"
    assert validPalindrome(s) == True

def test5():
    s = "ababc"
    assert validPalindrome(s) == False
