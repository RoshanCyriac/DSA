# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            return None
        current=head
        mid=head
        prev=head
        while current!=None and current.next!=None:
            prev=mid
            mid=mid.next
            current=current.next.next
            

        prev.next=mid.next
        return head