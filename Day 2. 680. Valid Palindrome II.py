#Day 2
#680. Valid Palindrome II

class Solution:
    def validPalindrome(self, s: str) -> bool:
        l,r = 0, len(s)-1
        chance = 1
        #using two pointers l and r
        #iterate until they meet
        while(l < r):
            #match characters
            if s[l] == s[r]:
                l+=1
                r-=1
            #incase of mismatch
            else:
                if chance > 0:
                    #check by deleting right
                    flag = True
                    cr = r-1
                    cl = l
                    while (cl < cr):
                        if s[cl] == s[cr]:
                            cl+=1
                            cr-=1
                        else:
                            flag = False
                            break
                    #if loop runs successfully return True
                    if flag: return True
                    
                    #else check by deleting left
                    cl = l+1
                    cr = r
                    flag = True
                    while (cl < cr):
                        if s[cl] == s[cr]:
                            cl+=1
                            cr-=1
                        else:
                            flag = False
                            break
                    #return answer true or False 
                    return flag
                return False
        return True
