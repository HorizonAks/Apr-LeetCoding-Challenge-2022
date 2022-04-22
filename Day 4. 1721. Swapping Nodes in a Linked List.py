#Day 4.
#1721. Swapping Nodes in a Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Simple Solution
        1. convert linklist to array
        2. swap kth values in arr
        3. create new Linked List using array
        """

        #Convert Linked List to Array
        arr = []
        q = head
        while(q):
            arr.append(q.val)
            q = q.next

        root = None
        #swap kth values/nodes
        arr[k-1],arr[-k] = arr[-k],arr[k-1]

        #create new Linked List using array
        q = None
        for i in range(len(arr)):
            if root == None:
                root = ListNode(arr[i])
                q = root
            else:
                q.next = ListNode(arr[i])
                q = q.next
        return root
