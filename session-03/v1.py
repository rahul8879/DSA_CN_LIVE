# student = {
#     'name': 'John Doe',
#     'age': 21,
#     'courses': ['Math', 'Science', 'History']
# }
# print(student)
# print(student['name'])  # Output: John Doe
# student['age'] = 23
# print(student)  # Output: 23


# operations
# insert 
# search
#update
# delete
#traversal 


# easy problems
# pattern : Frequency map
nums = [1, 2, 2, 3, 1, 1]

def frequency_map(nums):
    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1
    return freq

# print(frequency_map(nums))


# easy : Contain duplicate

def contains_duplicate_1(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)

    return False

# same problems we can solve using dict or hasmap

def contains_duplicate_2(nums):
    num_dict = {}
    for num in nums:
        if num in num_dict:
            return True
        num_dict[num] = True
    return False


# test it
# print(contains_duplicate_1([1, 2, 3, 4]))  # Output: False
# print(contains_duplicate_2([1, 2, 3, 1]))  # Output: True



# easy : Return the index of the first character that occurs exactly once.
# examples
# eg 1.  s = "leetcode" output = 0
# eg 2.  s = "loveleetcode" output = 2
# eg 3.  s = "aabb" output = -1
# eg 4.  s = "" output = -1

def first_unique_char(s):
    # declare your dict
    freq = {}

    # pass 1 : count the occurance of char
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    # pass 2 : find the first unique char
    for i, ch in enumerate(s):
        if freq[ch] == 1:
            return i

    return -1

print(first_unique_char("leetcode"))
print(first_unique_char("loveleetcode"))
print(first_unique_char("aabb"))
print(first_unique_char(""))