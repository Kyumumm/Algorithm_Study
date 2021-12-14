class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def get_node(self, index):
        cur = self.head
        count = 0
        while count < index:
            cur = cur.next
            count += 1
        return cur

    def printAll(self):
        cur = self.head
        count = 0
        while cur.next is not None:
            cur = cur.next
            count += 1
        return count

    def get_kth_node_from_last(self, k):
        # 뒤에서부터 시작
        distance = self.printAll()
        node = self.get_node(distance - k)

        return node


linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)
linked_list.append(9)

print(linked_list.get_kth_node_from_last(2).data)  # 7이 나와야 합니다!
