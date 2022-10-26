from typing import List


def top_k_frequent(nums: List[int], k: int) -> List[int]:
    """
     Bucket Sort
     [1,1,1,2,3,100]

     count 0    1     2   3    4   5
     value   [100]  [2]  [1]  [x] [x]
    """
    count = {}
    freq = [[] for i in range(len(nums) + 1)]

    for n in nums:
        count[n] = 1 + count.get(n, 0)  # if n doesn't exist set to 0
    for n, c in count.items():
        freq[c].append(n)

    res = []
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res


if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print(top_k_frequent(nums, k))
