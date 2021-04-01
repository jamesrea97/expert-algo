"""Module contains questions, answers and solutions to problems"""

# Question 1: Two Number Sum
# -> Input: a non-empty array of integers and a target sum integer
# -> Output: an array of ordered pair of elements that sum up to target sum if exist; 
# else empty array

def two_number_sum(array: list[int], target_sum: int) -> list[int]:
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

def is_valid_subsequence(array: list[int], sequence: list[int]) -> bool:

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

def sorted_squared_array(array: list[int]) -> list[int]:
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


# Question 4: Tournament Winner
# Input: List of lists, the competitions, comprised of 2 elements for each team and a list of results
# containing either 0 if the left competitor won; 1 if the right competitor won (no ties possible).
# Output: Return winning competitor

def tournament_winner(competitions: list[list[str]], results: list[int]) -> str:
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


# Question 5: Non-constructible Change
# Input: an array of positive integers representing values of coins in possession
# Output: Minimum value that you cannot create with change from coins in array.

def non_constructive_change(coins: list[int]) -> int:
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
# -> This means that for the ith position in the sorted_coins, we can make all the values up to the coins up until ith position. 
# -> We now consider non_constructive_change + 1
# -> If the coin at ith + 1 is larger, it means we will not be able to use all our coins to make it since we require an additional 1
# -> If all coins are used, return sum all coins + 1


# Complexity for n coins
# Time: O(nlog(n)) - sorting array
# Space: O(1) 


# Question 6: Find Closest Value in BST
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







if __name__ == "__main__":
    pass