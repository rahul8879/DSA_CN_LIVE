def search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        # case A : left half [left....mid] is sorted
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                # target can not be in the sorted left half
                left = mid + 1

        # case b : otherwise, right half [mid.....right] is sorted
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1
        




# Case 1: Left half sorted, target left mein
print(search([4, 5, 6, 7, 0, 1, 2], 5))

# Case 2: Left half sorted, target right mein
print(search([4, 5, 6, 7, 0, 1, 2], 0))

print(search([6, 7, 0, 1, 2, 3, 4], 3))
