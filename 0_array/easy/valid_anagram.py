def is_anagram(s, t):
    if len(s) != len(t):
        return False
    count_s, count_t = {}, {}

    for i in range(len(s)):
        count_s[s[i]] = 1 + count_s.get(s[i], 0)  # 0 default value
        count_t[t[i]] = 1 + count_t.get(t[i], 0)
    return count_s == count_t


def is_anagram_2(s, t):
    return sorted(s) == sorted(t)


if __name__ == '__main__':
    anagram1 = "rat"
    anagram2 = "car"
    print(is_anagram(anagram1, anagram2))
    anagram1 = "anagram"
    anagram2 = "nagaram"
    print(is_anagram(anagram1, anagram2))
