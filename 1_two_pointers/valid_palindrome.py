def is_palindrome(s):
    l, r = 0, len(s) - 1
    while l < r:
        while l < r and not alphanum(s[l]):
            l += 1
        while l < r and not alphanum((s[r])):
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l += 1
        r -= 1
    return True


def alphanum(c):
    return (
        # ord give the ascii value
            ord("A") <= ord(c) <= ord("Z") or
            ord("a") <= ord(c) <= ord("z") or
            ord("0") <= ord(c) <= ord("9")
    )


def is_palindrome_2(s):
    new_sentence = ""
    for c in s:
        if c.isalnum():
            new_sentence += c.lower()
    return new_sentence == reversed(new_sentence)  # or new_sentence[::-1]


if __name__ == '__main__':
    sentence = "A man, a plan, a canal: Panama"
    print(is_palindrome(sentence))
    sentence = "race a car"
    print(is_palindrome_2(sentence))
