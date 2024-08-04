class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseList(self, head):
        prev = None
        current = head 
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node 
    
sol = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
reversed_head = sol.reverseList(head)
while reversed_head:
    print(reversed_head.val)
    reversed_head = reversed_head.next