class CustomQueue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        return self.queue.pop(0)

    def is_empty(self):
        return self.queue == []


class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


def insert_node(root_node, node_value):
    if root_node.data is None:
        root_node.data = node_value
    elif node_value <= root_node.data:
        if root_node.left_child is None:
            root_node.left_child = BSTNode(node_value)
        else:
            insert_node(root_node.left_child, node_value)
    elif root_node.right_child is None:
        root_node.right_child = BSTNode(node_value)
    else:
        insert_node(root_node.right_child, node_value)
    return "The node has been successfully inserted"


def pre_order_traversal(root_node):
    if not root_node:
        return
    print(root_node.data)
    pre_order_traversal(root_node.left_child)
    pre_order_traversal(root_node.right_child)


def in_order_traversal(root_node):
    if not root_node:
        return
    in_order_traversal(root_node.left_child)
    print(root_node.data)
    in_order_traversal(root_node.right_child)


def post_order_traversal(root_node):
    if not root_node:
        return
    post_order_traversal(root_node.left_child)
    post_order_traversal(root_node.right_child)
    print(root_node.data)


def level_order_traversal(root_node):
    if not root_node:
        return
    custom_queue = CustomQueue()
    custom_queue.enqueue(root_node)
    while not (custom_queue.is_empty()):
        root = custom_queue.dequeue()
        print(root.data)
        if root.left_child is not None:
            custom_queue.enqueue(root.left_child)
        if root.right_child is not None:
            custom_queue.enqueue(root.right_child)


def search_node(root_node, node_value):
    if root_node.data == node_value:
        print("The value is found")
    elif node_value < root_node.data:
        if root_node.left_child.data == node_value:
            print("The value is found")
        else:
            search_node(root_node.left_child, node_value)
    else:
        if root_node.right_child.data == node_value:
            print("The value is found")
        else:
            search_node(root_node.left_child, node_value)


def min_value_node(bst_node):
    current = bst_node
    while (current.left_child is not None):
        current = current.left_child
    return current


def delete_node(root_node, node_value):
    # T: O(logN) S:  O(logN)
    if root_node is None:
        return root_node
    if node_value < root_node.data:
        root_node.left_child = delete_node(root_node.left_child, node_value)
    elif node_value > root_node.data:
        root_node.right_child = delete_node(root_node.right_child, node_value)
    else:
        if root_node.left_child is None:
            temp = root_node.right_child
            root_node = None
            return temp

        if root_node.right_child is None:
            temp = root_node.left_child
            root_node = None
            return temp

        temp = min_value_node(root_node.right_child)
        root_node.data = temp.data
        root_node.right_child = delete_node(root_node.right_child, temp.data)
    return root_node


if __name__ == "__main__":
    new_bst = BSTNode(None)

    '''
                70
               /  \
            50    90
            / \   / \     
           30 60 80  100
          / |
         20 40
    '''
    newBST = BSTNode(None)
    insert_node(newBST, 70)
    insert_node(newBST, 50)
    insert_node(newBST, 90)
    insert_node(newBST, 30)
    insert_node(newBST, 60)
    insert_node(newBST, 80)
    insert_node(newBST, 100)
    insert_node(newBST, 20)
    insert_node(newBST, 40)
    # print(newBST.data)
    # print(newBST.leftChild.data)

    # pre_order_traversal(newBST)
    # in_order_traversal(newBST)
    # level_order_traversal(newBST)
    # search_node(newBST, 40)
    delete_node(newBST, 20)
    level_order_traversal(newBST)
