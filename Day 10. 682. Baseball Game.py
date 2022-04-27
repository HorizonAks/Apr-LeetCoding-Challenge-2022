#Day 10.
#682. Baseball Game

class Solution(object):
    def calPoints(self, ops):
        #create a stack
        stack = []
        
        # for all ops if anything other than int aquired pop 2 values from stack and perform desired op
        # else add the int to the stack
        for op in ops:
            if op == '+':
                stack.append(stack[-1] + stack[-2])
            elif op == 'C':
                stack.pop()
            elif op == 'D':
                stack.append(2 * stack[-1])
            else:
                stack.append(int(op))

        return sum(stack)
