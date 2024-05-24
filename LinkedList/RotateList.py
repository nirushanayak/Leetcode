# Given the head of a linked list, rotate the list to the right by k places.

 

# Example 1:


# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]
# Example 2:


# Input: head = [0,1,2], k = 4
# Output: [2,0,1]
 

# Constraints:

# The number of nodes in the list is in the range [0, 500].
# -100 <= Node.val <= 100
# 0 <= k <= 2 * 109

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if(head == None):
            return None
        dummyNode=ListNode(0,head)
        length,tail = 0,dummyNode
        while(tail and tail.next):
            length=length+1
            tail=tail.next
        k=k%length
        head=dummyNode
        for i in range(length-k):
            head=head.next
        tail.next=dummyNode.next
        dummyNode.next=head.next
        head.next=None
        return dummyNode.next