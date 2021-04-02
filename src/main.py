"""Module contains questions, answers and solutions to problems"""
from typing import List, Union
# Question: Two Number Sum
# -> Input: a non-empty array of integers and a target sum integer
# -> Output: an array of ordered pair of elements that sum up to target sum if exist;
# else empty array


def two_number_sum(array: List[int], target_sum: int) -> List[int]:
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

            if element == required_element and element_count.get(element) < 2:
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


# Question: Validate Subsequence
# Input: two non-empty arrays of integers
# Output: True if second array is a subset of the first array; False otherwise

def is_valid_subsequence(array: List[int], sequence: List[int]) -> bool:

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


# Question: Sorted Squared Array
# Input: a sorted non-empty array of integers
# Output: array of sorted squared elements in array

def sorted_squared_array(array: List[int]) -> List[int]:
    result = []

    i = 0
    j = len(array) - 1

    squared_array = [e * e for e in array]

    while j - i > -1:
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


# Question: Tournament Winner
# Input: List of lists, the competitions, comprised of 2 elements for each team and list of results
# containing either 0 if the left competitor won; 1 if the right competitor won (no ties possible).
# Output: Return winning competitor

def tournament_winner(competitions: List[List[str]], results: List[int]) -> str:
    competitors = {}

    for match in competitions:
        if not competitors.get(match[0]):
            competitors[match[0]] = 0
        if not competitors.get(match[1]):
            competitors[match[1]] = 0

    for result, match in zip(results, competitions):
        if result:
            competitors[match[0]] += 1
        else:
            competitors[match[1]] += 1

    winner = None
    max_score = 0
    for competitor, wins in competitors.items():
        if wins > max_score:
            winner = competitor
            max_score = wins

    return winner

# Tactic:
# -> Trick: Get all competitors and count wins for each competitor
# -> Return competitor with most wins

# Complexity for n games, k teams:
# Time: O(n) - iterating through the n matches in competions, the results and the competitors
# Space: O(k) - storing the teams


# Question: Non-constructible Change
# Input: an array of positive integers representing values of coins in possession
# Output: Minimum value that you cannot create with change from coins in array.

def non_constructive_change(coins: List[int]) -> int:
    sorted_coins = sorted(coins)

    non_constructive_change = 0
    for i in range(len(sorted_coins)):
        if non_constructive_change + 1 < sorted_coins[i]:
            break
        else:

            non_constructive_change += sorted_coins[i]

    return non_constructive_change + 1


# Tactic:
# -> Trick: Sort coins so that you can go through them in increasing order
# -> We built the solution from the ground up. Starting with a non_constructive_change = 0
# -> Suppose we are able to construct all values up and inclusive of non_constructive_change
# -> This means that for the ith position in the sorted_coins, we can make all the values up to the
#    coins up until ith position.
# -> We now consider non_constructive_change + 1
# -> If the coin at ith + 1 is larger, it means we will not be able to use all our coins to make it
#    since we require an additional 1
# -> If all coins are used, return sum all coins + 1

# Complexity for n coins
# Time: O(nlog(n)) - sorting array
# Space: O(1)


# Question: Find Closest Value in BST
# Input: BST (defined below) tree root node and a target int value
# Output: Closest value to target in BST

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def find_closest_value_in_BST(root: BST, target: int) -> int:

    def recursive_closest_value_in_BST(node: BST, target: int, closest: int) -> int:
        if node is None:
            return closest

        if abs(node.value - target) < abs(closest - target):
            closest = node.value

        if target > node.value:
            return recursive_closest_value_in_BST(node.right, target, closest)
        elif target < node.value:
            return recursive_closest_value_in_BST(node.left, target, closest)
        else:
            return node.value

    return recursive_closest_value_in_BST(root, target, root.value)

# Tactic:
# -> Go down the tree, choosing the branch that is closes to the target value
# -> Keeping track of the closest and returning this one when reaching the leaf of the tree

# Complexity for n coins
# Time: O(log(n)) - going down one branch of the tree
# Space: O(1)


# Question: Branch Sums
# Input: BinaryTree (defined below) root
# Output: an ordered (from left to right) array of branch sums

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branch_sums(root: BinaryTree) -> List[int]:

    def recursive_branch_sums(node: BinaryTree, sums: List[int], current_sum: int) -> None:
        if node is None:
            return

        current_sum += node.value
        if node.left is None and node.right is None:
            sums.append(current_sum)

        recursive_branch_sums(node.left, sums, current_sum)
        recursive_branch_sums(node.right, sums, current_sum)

    sums = []
    recursive_branch_sums(root, sums, 0)
    return sums

# Tactic:
# -> Create an array (this is passed by reference and so will be updated throughout the algorithm)
# -> If both children are None, current node must be a leaf and so we add the current_sum to sums

# Complexity for n coins
# Time: O(n) - visiting each node in case we have a one branch of n nodes tree
# Space: O(n) - visiting each node in case we have a one branch of n nodes tree


# Question: Node Depths
# Input: BinaryTree (defined below) root
# Output: a sum of each node's depth in the BinaryTree
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def node_depths(root: BinaryTree) -> int:

    def recursive_node_depths(node: BinaryTree, sum: int) -> int:
        if node is None:
            return 0

        return (sum +
                recursive_node_depths(node.left, sum + 1) +
                recursive_node_depths(node.right, sum + 1))

    return recursive_node_depths(root, 0)


# Tactic:
# -> If node is None, make it return 0 as not a depth
# -> At any node consider its depth and the depth of its left and right children

# Complexity for n coins
# Time: O(n) - visiting each node once
# Space: O(1)


# Question: Depth First Search
# Input: For a given Node (defined below) node, an array of already travelled Node names
# Output: an array that contains depth-first search node travelled from root, without repetition
class Node:
    def __init__(self, name: str):
        self.children = []
        self.name = name

    def add_child(self, name: str) -> None:
        self.children.append(Node(name))
        return self

    def depth_first_search(self, array: List[str]) -> List[int]:
        array.append(self.name)

        for child in self.children:
            child.depth_first_search(array)

        return array


# Tactic:
# -> Depth-first search relies on recursion and adding to the stack

# Complexity for v vertices and e edges
# Time: O(v + e) - visiting each vertex and edge in the tree
# Space: O(v) - storing each vertex value in the tree


# Question: Minimum Wasting Time
# Input: a non-empty array of n positive integers representing time to compete each of the n tasks
# Output: minimum amount of total waiting time for all queries

def minimum_wasting_time(queries: List[int]) -> int:
    sorted_queries = sorted(queries)

    total_wasted_time = 0

    for i in range(1, len(sorted_queries)):
        total_wasted_time += sum(sorted_queries[:i])
    return total_wasted_time

# Tactic:
# -> Shortest task first is optimal.
# -> You do not need to wait for the first element.
# -> For each element, you must wait the total of time for all previous elements

# Complexity for n tasks
# Time: O(n) - iterating through all tasks
# Space: O(1)


# Question: Class Photos
# Input: an array of reds height, an array of blues heights, both of the same size
# Rules: (1) All students wearing same color shirts must be same row, (2) Back row has larger height
# Output: True if Rules (1) and (2) can be constructed from reds and blues

def class_photos(reds: List[int], blues: List[int]) -> bool:

    sorted_reds = sorted(reds)
    sorted_blues = sorted(blues)

    back = []
    front = []
    if sorted_reds[0] < sorted_blues[0]:
        back = sorted_blues
        front = sorted_reds
    elif sorted_reds[0] > sorted_blues[0]:
        back = sorted_reds
        front = sorted_blues
    else:
        return False

    for f, b in zip(front, back):
        if f >= b:
            return False
    return True

# Tactic:
# -> Sort the list firsts.
# -> Compare each ith position in both lists to see if Rules apply

# Complexity for n elements in each list
# Time: O(nlog(n)) - sorting lists
# Space: O(1)


# Question: Remove Duplicates From Linked List
# Input: a LinkedList (defined below) head, where each node is organized in order
# Output: a LinkedList without any duplicates

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def remove_duplicate_from_linked_list(head: LinkedList):
    current_node = head

    while current_node is not None:
        next_node = current_node.next
        while next_node is not None and next_node.value == current_node.value:
            next_node = next_node.next

        current_node.next = next_node
        current_node = current_node.next

    return head


# Tactic:
# -> Skip the repetitions by finding the next non-repeated value

# Complexity for n links in LinkedList
# Time: O(n) - iterating through the nodes only once
# Space: O(1)


# Question: Nth Fibonacci
# Input: an positive integer
# Output: the nth Fibonacci number

def get_nth_fibonacci(n: int) -> int:
    if n == 1:
        return 0
    if n == 2:
        return 1
    return get_nth_fibonacci(n-1) + get_nth_fibonacci(n-2)

# Tactic:
# -> Use recursion

# Complexity for n tasks
# Time: O(n) - have to go through n stacks to reach the stopping condition
# Space: O(1)


# Question: Product Sum
# Input: an array that has integer or list that can also have integers (and so on)
# Output: Product sum (depth * integer) for each element the array

def product_sum(array: List[Union[int, list]]) -> int:
    def recursive_product_sum(array: List[Union[int, list]], depth: int, sum_: int):
        for e in array:
            if type(e) == list:
                sum_ += recursive_product_sum(e, depth + 1, 0)
            else:
                sum_ += e
        return sum * depth
    return recursive_product_sum(array, 1, 0)

# Tactic:
# -> Use recursion

# Complexity for n elements
# Time: O(n) - have to go through n stacks to reach the stopping condition
# Space: O(1)


# Question: Binary Search
# Input: a sorted array of integers and a target value
# Output: the index of the target value; -1 if such index does not exist.

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

# Tactic:
# -> Only consider half of the elements at each iteration since sorted.

# Complexity for n elements
# Time: O(log(n)) - halving the search space every time
# Space: O(1)


# Question: Find Three Largest Numbers
# Input: an array of at least three numbers
# Output: an array of the three largest elemens in array

def find_three_largest_elements(array: List[int]) -> int:
    result = [array[0], array[1], array[2]]

    first = max(result)
    third = min(result)
    result.remove(first)
    result.remove(third)
    second = result[0]

    for i in range(3, len(array)):
        if array[i] > first:
            third = second
            second = first
            first = array[i]
        elif array[i] > second:
            third = second
            second = array[i]
        elif array[i] > third:
            third = array[i]
    return [third, second, first]

# Tactic:
# -> Get initial first, second, third.
# -> Consider remaining of the array, updating first/second/third as you iterate through it

# Complexity for n elements in array
# Time: O(n) - iterating through each element once
# Space: O(1)


# Question: Bubble Sort
# Input: an array of integers
# Output: a sorted array by Bubble Sort

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
# Tactic:
# -> Iterate through the list multiple times, swapping adjacent elements if they are not in order
# -> Stop when there are no more swaps since the list is then sorted

# Complexity for n elements in array
# Time: O(n^2) - if array is reversed sorted
# Space: O(1)


# Question: Insertion Sort
# Input: an array of integers
# Output: a sorted array by Insertion Sort

def insertion_sort(array: List[int]) -> List[int]:
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] < array[j - 1]:
            array[j], array[j-1] = array[j-1], array[j]
            j -= 1

    return array
# Tactic:
# -> Iterate through the list.
# -> As for each element keep swapping it with the previously sorted elements until it is in
#    the right position

# Complexity for n elements in array
# Time: O(n^2) - if array is reversed sorted
# Space: O(1)


# Question: Selection Sort
# Input: an array of integers
# Output: a sorted array by Insertion Sort

def selection_sort(array: List[int]) -> List[int]:
    for i in range(len(array)-1):
        lowest_value_index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[lowest_value_index]:
                lowest_value_index = j
        array[i], array[lowest_value_index] = array[lowest_value_index], array[i]

    return array

# Tactic:
# -> Iterate through the list , choosing the right value for the current index

# Complexity for n elements in array
# Time: O(n^2) - per position, we iterate through the array. n positions hence n * n = n^2
# Space: O(1)


# Question: Palindrom Check
# Input: a non empty string
# Output: True if the string is a palindrome; False otherwise

def is_palindrome(string: str) -> bool:
    i = 0
    j = len(string) - 1
    while j - i > -1:
        if string[i] != string[j]:
            return False
        j -= 1
        i += 1
    return True

# Tactic:
# -> Start with fist and last elements compare all elements same distance from middle of string

# Complexity for n elements in string
# Time: O(n) - iterating through the string once only
# Space: O(1)


# Question: Caesar Cipher Encryptor
# Input: a non empty string and an integer key
# Output: a string of the decoded string, constructed by shifting the letters by the key

def caesar_cipher_encryptor(string: str, key: int) -> str:
    result = ""

    for i in range(len(string)):
        ord_c = ord(string[i])
        new_ord = ((ord_c + key) - 97) % 26 + 97
        result += chr(new_ord)

    return result

# Tactic:
# -> Shift and use modulo to rebase back from 97 (ord of character 'a')

# Complexity for n elements in string
# Time: O(n) - iterating through the string once only
# Space: O(n) - result string


# Question Run-Length Encoding
# Input: a non-empty string
# Rule: 'AAAA' -> '4A' (max count is 9)
# Output: a string's run-length encoding

def run_length_encoding(string: str) -> str:
    result = ""

    i = 0

    while i < len(string):
        count = 1
        j = i + 1
        while j < len(string) and string[j] == string[i] and count < 9:
            count += 1
            j += 1
        result += f"{count}{string[i]}"
        i = j

    return result


# Tactic:
# -> Count number of instances of a character, stopping if exceeds 9

# Complexity for n elements in string
# Time: O(n) - iterating through the string once only
# Space: O(n) - result string

if __name__ == "__main__":
    pass
