# data = [[3,2,1],[1,2,1],[3,2,1]]

# output = []
# for i in data:
#     sum = 0
#     for j in i:
#         sum += j
#     output.append(sum)

# print(output)


def square_and_sort(nums):
    result = []
    for i in nums:
        result.append(i**2)
    result.sort()
    return result

# time complexity ---> O(n log n)
# space complexity ---> O(n)

nums = [-9,0,3,10,11]
result = square_and_sort(nums)
print(result)

# nums = [-4,-1,0,3,10]
# result = []
# for i in nums:
#     result.append(i**2)

# # sort it
# result.sort()

# print(result)
