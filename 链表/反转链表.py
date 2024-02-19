from typing import Optional


class ListNode:
    def __init__(self, val = 0, next = None):
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


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        cur = head
        while cur :
            tem = cur.next
            cur.next = pre
            pre = cur
            cur = tem
        return pre


arr = [1, 2, 3, 4, 5]

head = input_ListNone(arr)
solution = Solution()

head = solution.reverseList(head)
print_ListNone(head)