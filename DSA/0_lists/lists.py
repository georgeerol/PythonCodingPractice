if __name__ == '__main__':
    list = [1, 3, 5, 'seven']
    list.append(9)  # O(1)
    # inserts the element 2 at index 0
    list.insert(0, 2)  # O(n)
    # Remove the given element at a given index
    # Get runtime error if it doesn't exist
    list.remove('seven')  # O(n)
    # Remove Element at given index
    list.pop(2)  # O(n) or O(k) k <n
    list.reverse()  # O(n)

    # Slicing
    list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(list[1:])  # means all numbers greater than start uptil the range
    print(list[:4])  # means all numbers less than end uptil the range
    print(list[:])  # means all numbers within the range

    # Stepping
    print(list[0:9:2])

    # Initializing
    # means that the elements at positions 1, 2 and 3, up to but not including position 4, would be set to new values,
    list[1:4] = [45, 21, 83]
    print(list)

    # Delete
    # the empty start and end indices refer to 0 and length of the list by default, whereas 2 is the step size
    del list[::2]
    print(list)

    # Negative Indexing
    print(list[4:-1])  # 4, 5, 6, 7, 8
