"""Module contains important sorting algorithms"""
from typing import List


# Binary Search
def binary_search(array: List[int], target: int) -> int:
    start = 0
    end = len(array) - 1

    while end >= start:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif target < array[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1

# Complexity for n elements
# Time: O(log(n)) - halving the search space every time
# Space: O(1)


# Bubble Sort
def bubble_sort(array: List[int]) -> List[int]:
    while True:
        swaps = 0
        i = 1
        while i < len(array):
            if array[i - 1] > array[i]:
                swaps += 1
                array[i - 1], array[i] = array[i], array[i - 1]
            i += 1
        if swaps == 0:
            break

    return array

# Complexity for n elements in array
# Time: O(n^2) - if array is reversed sorted
# Space: O(1)
