
class BinaryThree:
    def __init__(self, size):
        self.custom_list = size * [None]
        self.last_used_index = 0
        self.max_size = size

    def insert_node(self, value):
        if self.last_used_index + 1 == self.max_size:
            return "The Binary Tree is full"
        self.custom_list[self.last_used_index + 1] = value
        self.last_used_index += 1
        return "The Value has been successfully inserted"

    def search(self, node_value):
        for i in range(len(self.custom_list)):
            if self.custom_list[i] == node_value:
                return "Success"
        return "Not found"

    def pre_order_traversal(self, index):
        if index > self.last_used_index:
            return
        print(self.custom_list[index])
        self.pre_order_traversal(index * 2)  # T O(n/2)
        self.pre_order_traversal(index * 2 + 1)  # S O(n)

    def in_order_traversal(self, index):
        if index > self.last_used_index:
            return
        print


if __name__ == "__main__":
    new_BT = BinaryThree(8)
    '''
                Drink
                /   \
              Hot    Cold
             /  \
            Tea  Coffee
    '''
    print(new_BT.insert_node("Drinks"))
    print(new_BT.insert_node("Hot"))
    print(new_BT.insert_node("Cold"))
    print(new_BT.insert_node("Tea"))
    print(new_BT.insert_node("Coffee"))

    print(new_BT.search("Tea"))
    print(new_BT.search("Hot"))

    new_BT.pre_order_traversal(1)
