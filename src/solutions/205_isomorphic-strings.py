from collections import Counter

def isIsomorphic(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    if not s and not t:
        return True
    
    map_hash = {}
    used = set()
    i = 0
    while i < len(s) and i < len(t):
        if s[i] not in map_hash:
            if t[i] in used:
                return False
            map_hash[s[i]] = t[i]
            used.add(t[i])
        else:
            if t[i] != map_hash[s[i]]:
                return False
        i += 1
    return True

def testEmpty():
    s, t = "", ""
    assert isIsomorphic(s, t) == True

def testTrue():
    s, t = "add", "egg"   # {"a": 1, "d": 2}  {"e": 1, "g": 2}
    assert isIsomorphic(s, t) == True

def testFalse():
    s, t = "erf", "wwf"
    assert isIsomorphic(s, t) == False

def testFalse2():
    s, t = "erff", "ffwd"
    assert isIsomorphic(s, t) == False
