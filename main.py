"""Module contains questions, answers and solutions to problems"""

# Question 1: Two Number Sum
# -> Input: a non-empty array of integers and a target sum integer
# -> Output: an array of ordered pair of elements that sum up to target sum if exist; 
# else empty array

def two_number_sum(array, target_sum):
    element_count = {}

    for e in array:
        if not element_count.get(e):
            element_count[e] = 1
        else:
            element_count[e] += 1
    
    for i in range(len(array)):
        element = array[i]
        required_element = target_sum - element
        if element_count.get(required_element):

            if element == required_element and element_count.get(element) <  2:
                pass
            else:
                return [element, required_element]
    return []

# Tactic: 
# -> Count occurrence of each element.
# -> Use Fact required_element = target_sum - element
# -> Consider edge case when required_element == element

# Complexity for n elements in array:
# Time: O(n) - iterating through the array (twice).
# Space: O(n)  - storing element_count


# Question 2: Validate Subsequence
# Input: two non-empty arrays of integers
# Output: True if second array is a subset of the first array; False otherwise

def is_valid_subsequence(array, sequence):

    i = 0
    j = 0

    while i < len(array) and j < len(sequence):
        if array[i] == sequence[j]:
            j += 1
        i += 1

    if j == len(sequence):
        return True

    return False

# Tactic: 
# -> Start at start of both array and sequence
# -> Move onto the next element in sequence only if exists in array (in order).
# -> If found all elements in sequence in array, return True; else False

# Complexity for n elements in array, m elements in sequence where m <= n:
# Time: O(n) - iterating through the array
# Space: O(1)


# Question 3: Sorted Squared Array
# Input: a sorted non-empty array of integers
# Output: array of sorted squared elements in array

def sorted_squared_array(array):
    result = []

    i = 0
    j = len(array) - 1

    squared_array = [e * e for e in array]

    while j -i > -1:
        if squared_array[i] > squared_array[j]:
            result.insert(0, squared_array[i])
            i += 1
        else:
            result.insert(0, squared_array[j])
            j -= 1
    
    return result
        
# Tactic: 
# -> Trick: negatives have positive squares
# -> Start at either side of the squared array.
# -> Insert into result array the largest at the start of the array.

# Complexity for n elements in array, m elements in sequence where m <= n:
# Time: O(n) - iterating through the array
# Space: O(n) - storing result array





if __name__ == "__main__":
    pass