from collections import Counter

def maxNumberOfBalloons(text: str) -> int:
    if not text:
        return 0
    
    text_freq = Counter(text)
    balloon_freq = Counter("balloon")
    res = float("inf")
    for c in balloon_freq:
        if c not in text_freq:
            return 0
        else:
            cnt = text_freq[c] // balloon_freq[c]
            if not cnt:
                return 0
            else:
                res = min(res, cnt)
    return res

def test1():
    text = "nlaebolko"
    assert maxNumberOfBalloons(text) == 1

def test2():
    text = "loonbalxballpoon"
    assert maxNumberOfBalloons(text) == 2

def test3():
    text = ""
    assert maxNumberOfBalloons(text) == 0
