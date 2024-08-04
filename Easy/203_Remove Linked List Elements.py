class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head, val):
        dummy = ListNode(0)
        dummy.next = head
        current = dummy

        while current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next

        return dummy.next

# دالة مساعدة لإنشاء قائمة مرتبطة من قائمة عادية
def create_linked_list(lst):
    dummy = ListNode(0)
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

# دالة مساعدة لتحويل القائمة المرتبطة إلى قائمة عادية
def linked_list_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# إنشاء القائمة المرتبطة
head = create_linked_list([1, 6, 6, 3, 4, 6, 5])

# إنشاء كائن الحل وتطبيق الدالة
solution = Solution()
new_head = solution.removeElements(head, 6)

# طباعة النتيجة
print(linked_list_to_list(new_head))