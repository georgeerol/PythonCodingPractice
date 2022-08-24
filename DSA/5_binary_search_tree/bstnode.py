class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


def insert(root_node, node_value):
    # T O(logN) S O(logN)
    if root_node.data is None:
        root_node.data = node_value
    # left side
    elif node_value <= root_node.data:
        if root_node.left_child is None:
            root_node.left_child = BSTNode(node_value)  # O(n/2)
        else:
            insert(root_node.left_child, node_value)

    # right side
    else:
        if root_node.right_child is None:
            root_node.right_child = BSTNode(node_value) # O(n/2)
        else:
            insert(root_node, node_value)
    return "The node has been successfully inserted"


if __name__ == "__main__":
    new_bst = BSTNode(None)
    print(insert(new_bst, 70))
    print(insert(new_bst, 60))
    print(new_bst.data)
    print(new_bst.left_child.data)
