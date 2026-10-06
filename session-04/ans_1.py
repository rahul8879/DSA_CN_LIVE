def binary_search(array,target):
    left = 0
    right = len(array) - 1
    while left <= right:
        # find the middle value
        middle = (left + right) // 2
        if array[middle] == target:
            return middle
        
        elif array[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    return -1


print(binary_search([8], 8))

# To apply binary search
# make sure your input should be sorted and increasing order
# there should not be any duplicate values


# Leetcode interview questions
# Given a sorted array of distinct integers, 
# return the target’s index, or −1 if absent. 
# Do not use list.index().

# [2,5,8,13,19], 13 → 3
# [2,5,8,13,19], 7 → −1
# [], 8 → −1
# [8], 8 → 0