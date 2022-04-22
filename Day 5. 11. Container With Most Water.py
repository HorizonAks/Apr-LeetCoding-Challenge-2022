#Day 5
#11. Container With Most Water

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        mv = 0
        #two pointers left and right
        while(left < right):
            #if height of left less than right update left
            if height[left] < height[right]:
                small = left
            else:
                #and vice versa
                small = right
            cv = height[small] * (right - left)
            #keey track of max amount of water
            mv = max(mv,cv)
            if small == left: left+=1
            if small == right: right-=1
        return mv
