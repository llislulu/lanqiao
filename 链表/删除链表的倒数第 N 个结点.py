from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def input_ListNone(arr: []):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def print_ListNone(head):
    current = head
    while current is not None:
        print(current.val, end='->')
        current = current.next
    print('None')


# 笨方法
# class Solution:
#     def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
#         dummy_head = ListNode(next=head)
#         curr_1 = dummy_head
#         curr = dummy_head
#         count = -1
#         while curr_1:
#             count += 1
#             curr_1 = curr_1.next
#         print(count)
#         for i in range(count-n):
#             curr = curr.next
#         curr.next = curr.next.next
#         return dummy_head.next

# 双指针法
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_head = ListNode(next=head)
        fast = dummy_head
        slow = dummy_head
        for i in range(n + 1):
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy_head.next


arr = [1, 2, 3, 4, 5]

head = input_ListNone(arr)
solution = Solution()

head = solution.removeNthFromEnd(head, 2)
print_ListNone(head)
