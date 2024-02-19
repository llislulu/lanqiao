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
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        while fast != None and fast.next !=None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:#公式 x = （y+z）（n-1）+z
                index1 = fast
                index2 = head
                while index2 != index1:
                    index1 = index1.next
                    index2 = index2.next
                return index2
        return None
