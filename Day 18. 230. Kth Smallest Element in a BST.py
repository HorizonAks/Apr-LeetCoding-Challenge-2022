#Day 18
#230. Kth Smallest Element in a BST

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        elements = []
        q = [root]
        while q:
            ele = q.pop(0)
            elements.append(ele.val)
            if ele.left:
                q.append(ele.left)
            if ele.right:
                q.append(ele.right)
        elements.sort()
        return elements[k-1]
