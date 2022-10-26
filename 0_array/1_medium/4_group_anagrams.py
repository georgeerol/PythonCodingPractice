from collections import defaultdict


def group_anagram(strs):
    # O(m*n)
    res = defaultdict(list)  # mapping charCount to List of Anagrams
    for s in strs:
        count = [0] * 26  # a ... z
        for c in s:
            count[ord(c) - ord("a")] += 1
        res[tuple(count)].append(s)
    return res.values()


def group_anagram_2(strs):
    res = defaultdict(list)  # mapping charCount to List of Anagrams.
    for s in strs:
        # keys can be strings, because they are immutable.
        res[str(sorted(s))].append(s)
    return res.values()


if __name__ == '__main__':
    strs = {"eat", "tea", "tan", "ate", "nat", "bat"}
    print(group_anagram_2(strs))
