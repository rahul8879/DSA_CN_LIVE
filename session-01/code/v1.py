nums = [-4,-1,0,3,10]
result = [0] * len(nums)
print(result)


def sorted_squared(array):
    i = 0
    j = len(array) - 1
    new_array = [0] * len(nums)
    for k in reversed(range(len(array))):
        print('value of k:', k)
        sq_i = array[i] ** 2
        sq_j = array[j] ** 2
        if sq_i > sq_j:
            new_array[k] = sq_i
            i += 1
        else:
            new_array[k] = sq_j
            j -= 1
    return new_array

print(sorted_squared(nums))
        
