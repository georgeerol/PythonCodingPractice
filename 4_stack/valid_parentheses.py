def is_valid(s):
    map = {")": "(", "]": "[", "}": "{"}
    stack = []

    for c in s:
        if c not in map:
            if stack and stack[-1] == map[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)
    return True if not stack else False

def is_valid_2(s):
    Map = {")": "(", "]": "[", "}": "{"}
    stack = []

    for c in s:
        if c not in Map:
            stack.append(c)
            continue
        if not stack or stack[-1] != Map[c]:
            return False
        stack.pop()

    return not stack


if __name__ == '__main__':
    s = "()[]{}"
    print(is_valid_2(s))
