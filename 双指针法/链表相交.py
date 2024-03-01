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
            lenA += 1
        curA = headA
        curB = headB
        if lenA > lenB:
            curA, curB = curB, curA
            lenA, lenB = lenB, lenA
        for _ in range(lenB - lenA):
            curB = cur.next
        while curA:
            if curA == curB:
                return curA
            else:
                curA = curA.next
                curB = curB.next
        return None


def input_ListNode(arr: []) -> ListNode:
    if not arr:
        return None
    head = arr[0]
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def print_ListNode(head) -> None:
    cur = head
    while cur:
        print(cur.val, end='->')
        cur = cur.next
    print("None")


