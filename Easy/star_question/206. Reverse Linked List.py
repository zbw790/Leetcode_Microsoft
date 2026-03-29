# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head != None:
            if head.next != None:
                return self.reverseListRecur(None, head, head.next)
            else:
                return head

    def reverseListRecur(self, previous_node, current_node, next_node):
        current_node.next = previous_node
        if next_node != None:
            final_node = self.reverseListRecur(current_node, next_node, next_node.next)
        else:
            return current_node

        return final_node

        

