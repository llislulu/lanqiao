
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeElements(self, head: ListNode, val: int):
        while head != None and head.val == val:
            head = head.next
        current = head
        while current != None and current.next != None:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        return head

def input_ListNone(arr:[]):
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
        print(current.val,end='->')
        current = current.next
    print('None')

arr = [6,6]
val = 6

head = input_ListNone(arr)
solution = Solution()
cur = solution.removeElements(head,val)
print_ListNone(cur)