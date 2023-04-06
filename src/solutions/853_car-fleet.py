from typing import List
from collections import defaultdict

# 12.07 first try, brute force way, 碰到target = 20 position = [6,2,17] speed = [3,9,2]的时候没能过
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # car/fleet (idx, speed, pos) at given time
        # we return when there's only 1 fleet in the field
        cars = [[]] * len(position)
        fleet = 0

        for i, v in enumerate(position):
            cars[i] = [i, speed[i], v]
            #           [i, speed, pos]

        while len(cars) > 1:
            now = defaultdict(list)
            new_cars = []
            for car in cars:
                car[2] = car[2] + car[1]
                now[car[2]].append((car[0], car[1]))
            for k, v in now.items():
                if k >= target:
                    fleet += 1
                else:
                    min_speed = float("inf")
                    for _, speed in v:
                        min_speed = min(min_speed, speed)
                    new_cars.append([v[0][0], min_speed, k])
            cars = new_cars
        
        return fleet + 1 if cars else fleet

# neet code的解。本来应该是O(n)但因为要sort所以是O(nlogn) M也是O(n)
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(p, s) for p, s in zip(position, speed)]
        cars.sort(reverse=True) #sort by descending position
        stack = []

        for p, s in cars:
            t = (target - p) / s # the time needed for a car to reach destination
            stack.append(t) # append the time needed to stack, from closest-to-destination(first) car to furtherest car
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop() # if first car takes 3 secs to reach desti and second takes 2, they will become a fleet 
                # and the fleet will continue to run with the speed of first (it must be the slower one), so we pop the 2nd
        
        return len(stack)


# 12.08 复习，模糊记得解法但记不清楚细节。尤其不记得为什么前两个车合并以后就可以pop，不用再考虑后面的车是否能和他们合并了
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # stack = [] # (position, time needed to reach target)

        cars = zip(position, speed)
        cars.sort(reverse = True)

        for i in range(len(cars)):
            if cars[i]:
                pass


# 12.15 复习还记得，感觉自己就是背下来了
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(p, (target - p) / s) for p, s in zip(position, speed)] # [(position, time needed to get to target)]
        cars.sort() # sort by asc position
        fleet = []

        for i in range(len(cars) - 1, -1, -1):
            fleet.append(cars[i][1])
            if len(fleet) >= 2 and fleet[-1] <= fleet[-2]:
                fleet.pop()
        
        return len(fleet)

# 1.2 复习还记得
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(p, s, (target - p) / s) for p, s in zip(position, speed)]
        cars.sort(key=lambda x: x[0], reverse=True) # sort by postion hight to low
        stack = []

        for car in cars:
            if stack and stack[-1][2] >= car[2]:
                continue
            else:
                stack.append(car)
        
        return len(stack)
            