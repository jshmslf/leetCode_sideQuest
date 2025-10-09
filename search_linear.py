"""linear Search
aka sequential search. It iterates through each array comparing 
it until to find its match.

Sorted or not sorted, it is fine.
"""

# Sample
arr = [1, 2, 3, 4 ,5 ,6 ,7]
target = 2

# it should return index and inside of the array

def LinearSearch(nums: list[int], target: int) -> bool:
    count = 0
    for i in range(len(nums)):
        count += 1
        if target == nums[i]:
            return True, print(f"the target ({target}) is in index {i}, the step is {count}")
    
    return False, print("Target is not found")
        
LinearSearch(arr, target)