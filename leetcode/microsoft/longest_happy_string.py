import heapq


# https://www.youtube.com/watch?v=8u-H6O_XQKE&ab_channel=NeetCode
def longest_diverse_string(a, b, c):
    res, max_heap = "", []
    for count, char in [(-a, "a"), (-b, "b"), (-c, "c")]:  # python doesn't have max heap so use neg value
        if count != 0:
            heapq.heappush(max_heap, (count, char))

    while max_heap:
        count, char = heapq.heappop((max_heap))
        if len(res) > 1 and res[-1] == res[-2] == char:
            if not max_heap:
                break
            count2, char2 = heapq.heappop(max_heap)
            res += char2
            count2 += 1
            if count2:
                heapq.heappush(max_heap, (count, char2))
        else:
            res += char
            count += 1
        if count:
            heapq.heappush(max_heap, (count, char))
    return res


def longest_diverse_string_2(a, b, c):
    mapping = [["a", a], ["b", b], ["c", c], ]
    z = a + b + c + 1
    res = []

    while z > 0:

        mapping.sort(key=lambda x: x[1], reverse=True)

        t0, c0 = mapping[0]
        t1, c1 = mapping[1]

        if c0 and res[-2:] != [t0, t0]:
            res.append(t0)
            mapping[0][1] -= 1

        elif c1:
            res.append(t1)
            mapping[1][1] -= 1

        z -= 1

    return "".join(res)


if __name__ == '__main__':
    a = 1
    b = 1
    c = 7
    print(longest_diverse_string(a, b, c))
    print(longest_diverse_string_2(a, b, c))
