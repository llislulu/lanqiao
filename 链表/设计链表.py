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


class MyLinkedList:

    def __init__(self):
        self.dummy_head = ListNode()
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        current = self.dummy_head.next
        for i in range(index):
            current = current.next
        return current.val

    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val, self.dummy_head.next)
        self.dummy_head.next = new_node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val)
        current = self.dummy_head
        while current.next:
            current = current.next
        current.next = new_node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        current = self.dummy_head
        for i in range(index):
            current = current.next
        current.next = ListNode(val, current.next)
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        current = self.dummy_head
        for i in range(index):
            current = current.next
        current.next = current.next.next
        self.size -= 1


# 初始化 MyLinkedList 对象
mylist = MyLinkedList()
# 在头部添加节点 7
mylist.addAtHead(7)
print_ListNone(mylist.dummy_head.next)
# 在头部添加节点 2
mylist.addAtHead(2)
print_ListNone(mylist.dummy_head.next)
# 在头部添加节点 1
mylist.addAtHead(1)
print_ListNone(mylist.dummy_head.next)
# 在索引 3 处插入节点 0
mylist.addAtIndex(3, 0)
print_ListNone(mylist.dummy_head.next)
# 删除索引 2 处的节点
mylist.deleteAtIndex(2)
print_ListNone(mylist.dummy_head.next)
# 再次在头部添加节点 6
mylist.addAtHead(6)
print_ListNone(mylist.dummy_head.next)
# 在尾部添加节点 4
mylist.addAtTail(4)
print_ListNone(mylist.dummy_head.next)
print(mylist.size)
# 获取索引 4 处的节点值
print(mylist.get(4))  # 预期输出: 4

# 再次在头部添加节点 4
mylist.addAtHead(4)

# 在索引 5 处插入节点 5
mylist.addAtIndex(5, 5)

# 再次在头部添加节点 6
mylist.addAtHead(6)

