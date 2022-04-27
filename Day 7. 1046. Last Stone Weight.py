#Day 7.
#1046. Last Stone Weight

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #simulate the problem
        while(len(stones) > 1):
            #pick 2 heaviest stones
            h1 = stones.pop(stones.index(max(stones)))
            h2 = stones.pop(stones.index(max(stones)))
            #smash them
            r = h1-h2
            #add to list if remainder is created
            if r != 0:
                stones.append(r)
        return stones[0] if stones else 0
