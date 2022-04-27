#Day 20
#173. Binary Search Tree Iterator


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
                
    def makeIn(self,root):
        if root == None: return
        self.makeIn(root.left)
        self.inorder.append(root.val)
        self.makeIn(root.right)

    def __init__(self, root: Optional[TreeNode]):
        self.inorder = [-1]
        self.makeIn(root)
        self.pointer = 0

    def next(self) -> int:
        self.pointer+=1
        return self.inorder[self.pointer]
    
    def hasNext(self) -> bool:
        #print(self.pointer,self.inorder)
        return self.pointer < len(self.inorder)-1
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
