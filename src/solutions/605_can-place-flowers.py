from typing import List

def canPlaceFlowers(flowerbed: List[int], n: int) -> bool:
    # 1, 0, 0, 0, 1 ---> 1 ---> 1: 1
    # 0, 0, 0, 0, 1 ---> 2 -----> 3: 2
    # 1, 0, 0, 0, 0, 1 ---> 1 -----> 2: 1
    # find continuous 0s
    # neighbors of 1s can't be used
    # after we get the length of 0s, flower # = if odd (n + 1) // 2, if even n // 2
    cur_len = 0
    continuous_0s = []
    canUse = True

    for p in flowerbed:
        if p == 1:
            if cur_len > 1:
                continuous_0s.append(cur_len - 1)
            canUse = False
            cur_len = 0
            continue
        else:
            if not canUse:
                canUse = True
                continue
            else:
                cur_len += 1
    if cur_len:
        continuous_0s.append(cur_len)
    
    res = 0
    for len_0 in continuous_0s:
        if len_0 % 2 == 0:
            res += len_0 // 2
        else:
            res += (len_0 + 1) // 2
    return res >= n

def testFalse():
    flowerbed = [1,0,0,0,1]
    assert canPlaceFlowers(flowerbed, 2) == False

def testTrue():
    flowerbed = [1,0,0,0,1]
    assert canPlaceFlowers(flowerbed, 1) == True

def testFalse2():
    flowerbed = [1,1]
    assert canPlaceFlowers(flowerbed, 1) == False

def testTrue2():
    flowerbed = [0]
    assert canPlaceFlowers(flowerbed, 1) == True