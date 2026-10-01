# `nums = [2, 7, 11, 15], target = 9 → [0, 1]`
# different test cases
# `nums = [3, 2, 4], target = 6 → [1, 2]`
# `nums = [3, 3], target = 6 → [0, 1]`


# edges cases --> production issue
# `nums = [2, 7, 11, 15], target = -4 → []`
# num = [] target = 21 → []
# time complexity O(n^2)
# space complexity O(1)
def two_sum_brute(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

# print(two_sum_brute([2, 7, 11, 15], 9))  # Output: [0, 1]

assert two_sum_brute([2, 7, 11, 15], 9) == [0, 1]
assert two_sum_brute([3, 2, 4], 6) == [1, 2]
assert two_sum_brute([3, 3], 6) == [0, 1]
assert two_sum_brute([2, 7, 11, 15], -4) == []
assert two_sum_brute([], 21) == []


def two_sum(nums, target):
    seen= {}
    for i, value in enumerate(nums):
        needed = target - value
        if needed in seen:
            return [seen[needed], i]
        seen[value] = i
    return []


# time complexity O(n)
# space complexity O(n)

# print(two_sum([2, 7, 11, 15], 9))  # Output: [0, 1]
# print(two_sum([3, 2, 4], 6))       # Output: [1, 2]
# print(two_sum([3, 3], 6))          # Output: [0, 1]
# print(two_sum([2, 7, 11, 15], -4)) # Output: []
# print(two_sum([], 21))             # Output: []


# PS : Move zeroes to the end **in place**, preserving the order of nonzero elements.
# eg. 1 [0, 1, 0, 3, 12] → [1, 3, 12, 0, 0]
# eg. 2 [0, 0, 1] → [1, 0, 0]
# eg. 3 [1, 2, 3] → [1, 2, 3]

# ask many to interviewers ??
# can my input contain duplicates?
# what if I have negative numbers?

def move_zeroes(nums):
    write = 0
    for read in range(len(nums)):
        if nums[read] != 0:
            nums[write] = nums[read]
            write += 1
    for i in range(write, len(nums)):
        nums[i] = 0

    return nums

# print(move_zeroes([0, 1, 0, 3, 12]))
# print(move_zeroes([0, 0, 1]))
# print(move_zeroes([1, 2, 3]))


# time complexity O(n)
# space complexity O(1)

# try it by yourself
# Ignore non-alphanumeric characters and 
# letter case; check whether the remaining 
# string reads the same both ways.

# eg 1 : "A man, a plan, a canal: Panama" → True
# eg 2 : "race a car" → False
# eg 3 : " " → True



# sliding windows 

def length_of_longest_substring(s):
    seen = set() # store char in current windows
    left = 0
    best = 0
    for right, char in enumerate(s):
        # if duplicate
        while char in seen:
            seen.remove(s[left])
            left += 1
        seen.add(char)
        best = max(best, right - left + 1)
    return best


# print(length_of_longest_substring("abcdasdad"))
# print(length_of_longest_substring("race a car"))
# print(length_of_longest_substring(" "))

# Problem 5 — Maximum Average Subarray I (LeetCode 643
# **Goal:** Find the maximum average among 
# contiguous subarrays of exactly `k` 
# elements, where `1 <= k <= len(nums)`.

# **Example:** `[1, 12, -5, -6, 50, 3], k = 4 → 12.75`

def max_avg(num,k):
    window_sum = 0
    for i in range(k):
        window_sum += num[i]
    best = window_sum
    for right in range(k, len(num)):
        window_sum = window_sum + num[right] - num[right - k]
        best = max(best, window_sum)
    return best / k
print(max_avg([1, 12, -5, -6, 50, 3], 4))

#  Minimum Size Subarray Sum (LeetCode 209)
# For **positive integers** and a positive target,
# find the shortest contiguous subarray with 
# sum at least the target. Return 0 if none exists.

### Problem 8 — Range Sum Query: Immutable (LeetCode 303)

# **Goal:** Answer many inclusive 
# range-sum queries on an array that does not change.

# **Example:** `nums = [3, 2, 4, 1, 5]`, 
# query `(1, 3) → 7`.


class NumArray:

    def __init__(self, nums):
        self.nums = nums
        self.prefix_sum = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.prefix_sum[i + 1] = self.prefix_sum[i] + nums[i]

    def sum_range(self, left, right):
        return self.prefix_sum[right + 1] - self.prefix_sum[left]
    
obj = NumArray([3, 2, 4, 1, 5])
print(obj.sum_range(0,4))  # Output: 7


# Subarray Sum Equals K (LeetCode 560)
# **Goal:** Count all contiguous subarrays with 
# sum exactly `k`. Values may be positive, zero, or negative.
# **Example:** `[1, 1, 1], k = 2 → 2`.
