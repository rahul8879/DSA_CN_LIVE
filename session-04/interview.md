# Binary Search — Interview Practice Problems

## Problem 1: Search Insert Position

You are given an integer array `nums`, sorted in ascending order with distinct values, and an integer `target`.

Return the index of `target` if it exists. Otherwise, return the index where `target` should be inserted so that the array remains sorted.

Your algorithm must run in **O(log n)** time.

You do not need to actually insert the element. Return only the index.

### Example 1

- **Input:** `nums = [1, 3, 5, 6], target = 5`
- **Output:** `2`
- **Explanation:** `5` already exists at index `2`.

### Example 2

- **Input:** `nums = [1, 3, 5, 6], target = 2`
- **Output:** `1`
- **Explanation:** Inserting `2` at index `1` would produce `[1, 2, 3, 5, 6]`.

### Example 3

- **Input:** `nums = [1, 3, 5, 6], target = 7`
- **Output:** `4`
- **Explanation:** `7` would be inserted after the last element.

### Assumptions

- The array is non-empty.
- All values are distinct.
- The array is sorted in ascending order.
- Indices start at `0`.




## Problem 2: Find Minimum in a Rotated Sorted Array

You are given a non-empty integer array `nums` containing distinct values.

The array was originally sorted in ascending order and may have been rotated.

For example, `[0, 1, 2, 4, 5, 6, 7]` can become `[4, 5, 6, 7, 0, 1, 2]` after rotation.

Return the **smallest value** in the array.

Your algorithm must run in **O(log n)** time.

### Example 1

- **Input:** `nums = [4, 5, 6, 7, 0, 1, 2]`
- **Output:** `0`
- **Explanation:** The smallest value is `0`. Return its value, not its index.

### Example 2

- **Input:** `nums = [3, 4, 5, 1, 2]`
- **Output:** `1`
- **Explanation:** The smallest value is `1`.




## Problem 4: Find a Peak Element

You are given a non-empty integer array `nums`. Adjacent elements are never equal.

A **peak element** is an element strictly greater than its immediate neighbours.

Return the **index of any one peak**.

If multiple peaks exist, any peak index is acceptable.

For boundary elements, assume the value outside either end of the array is negative infinity.

Your algorithm must run in **O(log n)** time.

### Example 1

- **Input:** `nums = [1, 2, 3, 1]`
- **Output:** `2`
- **Explanation:** The value `3` at index `2` is greater than both neighbours, `2` and `1`.

### Example 2

- **Input:** `nums = [1, 3, 2, 4, 1]`
- **Output:** `1` or `3`
- **Explanation:** Both `3` at index `1` and `4` at index `3` are peaks. Return either index.

### Example 3

- **Input:** `nums = [1, 2, 3, 4]`
- **Output:** `3`
- **Explanation:** The last element `4` is greater than its left neighbour. Its imaginary right neighbour is negative infinity.

### Example 4

- **Input:** `nums = [5]`
- **Output:** `0`
- **Explanation:** Both imaginary neighbours are negative infinity, so the only element is a peak.

### Assumptions

- The array is non-empty.
- The array is not necessarily sorted.
- Adjacent elements are never equal.
- A peak need not be the largest value in the entire array.
- Return one peak index, not its value or a list of all peaks.


---
