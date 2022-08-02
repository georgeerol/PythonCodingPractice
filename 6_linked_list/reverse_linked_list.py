# Definition for singly-linked list.
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def reverse(self):
        prev, curr = None, self.head
        # T O(n) M O(1)
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        self.head = prev

    def reverse_r(self, head):
        # recursive: t O(n) M (O)
        if not head or not head.next:
            return head
        p = self.reverse_r(head.next)
        head.next.next = head
        head.next = None
        self.head = p

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next


if __name__ == '__main__':
    llist = LinkedList()
    llist.push(2)
    llist.push(1)
    #llist.reverse()
    #llist.print_list()
    llist.reverse_r(llist.head)
    llist.print_list()

