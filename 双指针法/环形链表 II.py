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
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                index1 = head
                index2 = fast
                while index1 != index2:
                    index1 = index1.next
                    index2 = index2.next
                return index1
        return None

arr = [1, 2, 3, 4]
head = input_ListNone(arr)
cur = head
cur2 = head.next.next
while cur.next != None:
    cur = cur.next

cur.next = cur2
solution = Solution()
a = solution.detectCycle(head)
print(a.val)
