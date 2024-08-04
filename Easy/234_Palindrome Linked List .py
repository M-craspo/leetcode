
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def isPalindrome(self, head):
        l =[]
        while head:
            l.append(head.val)
            head = head.next
        return l == l[::-1]
    

    def isPalindrome(self, head):

        if not head or not head.next:  
            return True

        slow = fast = head
        while fast and fast.next:  
            slow = slow.next
            fast = fast.next.next

        prev = None
        curr = slow  
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        while head and prev:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next

        return True
