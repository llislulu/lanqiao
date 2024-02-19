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


def reverse(cur: Optional[ListNode], pre: Optional[ListNode]):
    if cur == None:
        return pre
    tem = cur.next
    cur.next = pre
    return reverse(tem, cur)


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return reverse(head,None)


arr = [1, 2, 3, 4, 5]

head = input_ListNone(arr)
solution = Solution()

head = solution.reverseList(head)
print_ListNone(head)