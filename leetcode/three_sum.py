def find_triplets(arr):
    found = False
    array_length = len(arr)
    for i in range(array_length - 1):
        s = set()
        for j in range(i + 1, array_length):
            x = -(arr[i] + arr[j])
            if x in s:
                print(x, arr[i], arr[j])
                found = True
            else:
                s.add(arr[j])
        if not found:
            print("No Triplet Found")


if __name__ == '__main__':
    arr = [0, -1, 2, -3, 1]
    find_triplets(arr)
