def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array

print(insertion_sort([64, 34, 25, 12, 22, 11, 90]))
print(insertion_sort([-5, -1, -15, -10]))


# what if I want to sort in decreasing order
def insertion_sort_descending(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key > array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array

print(insertion_sort_descending([64, 34, 25, 12, 22, 11, 90]))



# https://coddy.tech/visualize/sorting/insertion-sort