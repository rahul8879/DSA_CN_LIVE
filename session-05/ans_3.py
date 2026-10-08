# merge sort algorithm

a = [64, 34, 25, 12, 22, 11, 90]
b = [-5, -1, -15, -10]

# merge a and b into a single sorted array
def merge_sort(a, b):
    merged = []
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            j += 1
    # Append any remaining elements from either array
    merged.extend(a[i:])
    merged.extend(b[j:])
    return merged


print(merge_sort(a, b))