def find_first_unique(lst):
    # O(n^2) | O(1) space
    for i in range(len(lst)):
        j = 0
        while j < len(lst):
            if i != j and lst[i] == lst[j]:
                break
            j += 1
        if j == len(lst):
            return lst[i]
    return None


def find_first_unique_2(lst):
    # O(n^2) | O(1) space
    counts = {}
    counts = counts.fromkeys(lst, 0)
    for ele in lst:
        counts[ele] = counts[ele] + 1

    answer_key = None
    for ele in lst:
        if counts[ele] == 1:
            answer_key = ele
            break
    return answer_key


if __name__ == "__main__":
    lst = [1, 1, 1, 2, 3, 2, 4]
    print(find_first_unique(lst))
    print(find_first_unique_2(lst))
