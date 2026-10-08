def merge(interval):
    interval.sort(key=lambda x: x[0])  # Sort intervals based on the start time
    result =[interval[0]]

    for start, end in interval[1:]:
        last_end = result[-1][1]
        if start <= last_end:  # Overlapping intervals
            result[-1][1] = max(last_end, end)  # Merge intervals
        else:
            result.append([start, end])  # No overlap, add new interval

    return result

print(merge([[2, 6], [1, 3], [8, 10], [15, 18]]))