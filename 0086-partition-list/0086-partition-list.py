# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # dummy nodes for linked lists
        lesser = ListNode()  # for elements less than x
        equal_greater = ListNode()  # for elements equal or greater
        
        # pointers to iterate over linked lists
        i = lesser
        j = equal_greater

        while head:
            if head.val < x:
                i.next = head  # update next node pointer
                i = i.next  # update iteration pointer
            else:
                j.next = head  # update next node pointer
                j = j.next  # update iteration pointer

            head = head.next  # update head

        i.next = equal_greater.next  # connect linked lists
        j.next = None  # update next of last node

        return lesser.next  # the new head