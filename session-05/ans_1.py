def bubble_sort(array):
    sorted = False
    counter = 0
    while not sorted:
        sorted = True
        for i in range(len(array) - 1 - counter):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                sorted = False
        counter += 1
    return array

print(bubble_sort([64, 34, 25, 12, 22, 11, 90]))
print(bubble_sort([-5, -1, -15, -10]))


# what if I want to sort in decreasing order
def bubble_sort_descending(array):
    sorted = False
    counter = 0
    while not sorted:
        sorted = True
        for i in range(len(array) - 1 - counter):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                sorted = False
        counter += 1
    return array

print(bubble_sort_descending([64, 34, 25, 12, 22, 11, 90]))
print(bubble_sort_descending(['rahul', 23, 'mohit', 'ananya']))


# https://coddy.tech/visualize/sorting/bubble-sort