arr = [1, 2, 3, 4 ,5 ,6 ,7]
target = 7

# it should return index and inside of the array

def LinearSearch(nums: list[int], target: int) -> bool:
    count = 1
    for i in range(len(nums)):
        count += 1
        if target == nums[i]:
            return True, print(f"the target ({target}) is in index {i}, the step is {count}")
    
    return False, print("Target is not found")
        
LinearSearch(arr, target)