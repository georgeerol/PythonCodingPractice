class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = value


class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, value, location):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        elif location == 0:  # first
            new_node.next = self.head
            self.head = new_node
        elif location == 1:  # last
            new_node.next = None
            self.tail.next = new_node
            self.tail = new_node
        else:
            temp_node = self.head
            for _ in range(location - 1):
                temp_node = temp_node.next
            next_node = temp_node.next
            temp_node.next = new_node
            new_node.next = next_node
            if temp_node == self.tail:
                self.tail = new_node

    def delete(self, location):
        if self.head is None:
            print("The SLL does not exist")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            elif location == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = None
                    self.tail = node
            else:
                temp_node = self.head
                index = 0
                while index < location - 1:
                    temp_node = temp_node.next
                    index += 1
                next_node = temp_node.next
                temp_node.next = next_node.next

    def delete_entire(self):
        if self.head is None:
            print("The SLL does not exist")
        else:
            self.head = None
            self.tail = None

    def traverse(self):
        if self.head is None:
            print("The Singly Linked List does not exist")
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next

    def search(self, node_value):
        if self.head is None:
            return "The list does not exist"
        node = self.head
        while node is not None:
            if node.value == node_value:
                return node.value
            node = node.next
        return "The value does not exist in this list"

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next


if __name__ == '__main__':
    sLinkedList = SLinkedList()
    sLinkedList.insert(1, 1)
    sLinkedList.insert(2, 1)
    sLinkedList.insert(3, 1)
    sLinkedList.insert(4, 1)
    sLinkedList.insert(0, 0)
    sLinkedList.insert("x", 3)

    print([node.value for node in sLinkedList])
    sLinkedList.traverse()
    sLinkedList.delete(0)
    print([node.value for node in sLinkedList])
    sLinkedList.delete(2)
    print([node.value for node in sLinkedList])
