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


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(next=head)
        current = dummy_head
        while current.next is not None and current.next.next is not None:
            tmp = current.next#存1
            t = current.next.next#2
            t_2 = current.next.next.next#3
            current.next = t
            current.next.next = tmp
            current.next.next.next = t_2
            current = current.next.next
        return dummy_head.next
arr = [1, 2, 3, 4]

head = input_ListNone(arr)
solution = Solution()

head = solution.swapPairs(head)
print_ListNone(head)
