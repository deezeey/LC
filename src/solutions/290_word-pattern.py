def wordPattern(pattern: str, s: str) -> bool:
    if not pattern or not s:
        return False
    pattern_arr = list(pattern)
    s_arr = s.split(" ")
    if len(pattern_arr) != len(s_arr):
        return False
    return len(set(pattern_arr)) == len(set(s_arr)) == len(set(zip(pattern_arr, s_arr)))


def test1():
    pattern = "abba"
    s = "dog cat cat dog"
    assert wordPattern(pattern, s) == True

def test2():
    pattern = "abba"
    s = "dog cat cat fish"
    assert wordPattern(pattern, s) == False

def test3():
    pattern = "aaaa"
    s = "dog cat cat dog"
    assert wordPattern(pattern, s) == False

def test4():
    pattern = "aba"
    s = "cat cat cat dog"
    assert wordPattern(pattern, s) == False