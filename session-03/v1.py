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

# print(first_unique_char("leetcode"))
# print(first_unique_char("loveleetcode"))
# print(first_unique_char("aabb"))
# print(first_unique_char(""))

# easy 4 : valid anagram ==> oracle, databricks 

# what is anagram
# An anagram is a word or phrase formed by rearranging the 
# letters of a different word or phrase, typically using all the original letters exactly once.
# Two strings are anagrams if they contain exactly the 
# same characters with exactly the same counts.

# example 1 : "anagram" and "nagaram". ==> freq {a: 3, n: 2, g: 1, r: 1, m: 1} ===> true
# example 2 : "rat" and "car". ==> freq {r: 1, a: 1, t: 1, c: 1} ===> false

# examples : "listen" and "test". ==> freq {l: 1, i: 1, s: 1, t: 1, e: 1, n: 1} ===> false

def is_anagram(s, t):
    if len(s) != len(t):
        return False
    
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    for ch in t:
        if ch not in freq:
            return False
        freq[ch] -= 1
        if freq[ch] < 0:
            return False

    return True


    
    
# print(is_anagram("leet", "leet"))  # Output: True



# medium 1 : Return unique elements that appear in both arrays.

# examples : 
# arr1 = [1, 2, 2, 3]
# arr2 = [2, 3, 4]
# Output: [2, 3]

# example 2:
# arr1 = [5, 6, 7]
# arr2 = [7, 8, 9]
# Output: [7]

# examples 3
# arr1 = [1, 2, 3]
# arr2 = [-1, 4, 5]
# Output: []


def intersection(arr1, arr2):
    lookup = set(arr1)
    answer = set()
    for num  in arr2:
        if num in lookup:
            answer.add(num)

    return list(answer)

# print(intersection([1, 2, 2, 3], [4,5,6]))  # Output: [2, 3]

# medium 2 : group anagram 

# Group strings that are anagrams of each other. Example: ["eat","tea","tan","ate","nat","bat"]

# example 1 : input = words output = [["eat","tea","ate"],["tan","nat"],["bat"]]

# example 2 : input = words output = [["listen","silent"],["enlist","inlets"],["rat","tar"]]

def group_anagrams(words):
    group = {}

    for word in words:
        key = ''.join(sorted(word)) # nlogn
        if key not in group:
            group[key] = []
        group[key].append(word)

    return list(group.values())

# print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))
# print(''.join(sorted('ate')))

# time complexity : O(n * k log k) where n is the number of words and k is the maximum length of a word


# medium : top k frequent elements : EPAM/ oracle/ Databricks/Tiger analytics

# Return the k most frequent values. 
# First build value → count. Then organize values by their counts.


# example 1 : input = [1,1,1,2,2,3], k = 2
# Output: [1, 2]

# example 2 : input = [1,1,1,2,2,3], k = 1
# Output: [1]

# example 3 : input = [1,1,1,2,2,3], k = 3
# Output: [1, 2, 3]

# dont skip this one
def top_k_frequent(nums, k):
    freq = {}

    # occurance of char
    for num in nums:
        freq[num] = freq.get(num, 0) + 1

    sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    # pick the top k
    result = []
    for i in range(min(k, len(sorted_freq))):
        result.append(sorted_freq[i][0])
    return result


# print(top_k_frequent([1,1,1,2,2,3,34], 2))  # Output: [1, 2]

# Hard : Subarray Sum Equals K


# Count the number of continuous subarrays whose sum equals k.

# example 1:
# Input: nums = [1,1,1], k = 2
# Output: 2
# Explanation: The subarrays are [1,1] (from index 0 to 1) and [1,1] (from index 1 to 2).

# example 2:
# Input: nums = [1,2,3], k = 3
# Output: 2
# Explanation: The subarrays are [1,2] (from index 0 to 1) and [3] (from index 2 to 2).

# example 3:
# Input: nums = [1], k = 0
# Output: 0
# Explanation: There are no subarrays that sum to 0.

def subarray_sum(num,k):
    prefix_count = {0:1}
    prefix = 0
    answer = 0
    for n in num:
        prefix += n
        needed = prefix - k
        answer += prefix_count.get(needed, 0)
        prefix_count[prefix] = prefix_count.get(prefix, 0) + 1

    return answer

print(subarray_sum([1,1,1], 2))  # Output: 2
print(subarray_sum([1,2,-1], 3))  # Output: 2
print(subarray_sum([1], 0))  # Output: 0
