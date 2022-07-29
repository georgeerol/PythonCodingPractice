def merge(intervals):
    # O(nLogn)
    intervals.sort(key=lambda i: i[0])  # sorting from the start value

    output = [intervals[0]]

    # O(n)
    for start, end in intervals[1:]:
        last_end = output[-1][1]
        if start <= last_end:
            output[-1][1] = max(last_end, end)
        else:
            output.append([start, end])
    return output


if __name__ == '__main__':
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print(merge(intervals))
