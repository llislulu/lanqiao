class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        lenA, lenB = 0, 0
        cur = headA
        while cur:
            cur = cur.next
            lenA += 1
        cur = headB
        while cur:
            cur = cur.next
            lenB += 1
        cur_A = headA
        cur_B = headB
        if lenA > lenB:
            cur_A, cur_B = cur_B, cur_A
            lenA, lenB = lenB, lenA
        for _ in range(lenB - lenA):
            cur_B = cur_B.next
        while cur_A:
            if cur_A == cur_B:
                return cur_A
            else:
                cur_A = cur_A.next
                cur_B = cur_B.next
        return None


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
