"""Binary Search
It need a sorted list to continue the search.
The it will start in the middle to find it match.
Once it is greater that, it will be move in the right side,
when lower than, it will move in the left side.
"""

# make sure that the array is sorted
arr = [9, 7, 8, 6, 5, 4, 3, 2, 1]
temp = 0

def sort(nums: list[int]):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
    return nums

# sorted
arr = sort(arr) # [1, 2, 3, 4, 5, 6, 7, 8, 9]

def binarySearch(nums: list[int], target: int) -> bool:
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if target == arr[mid]:
            return True, print(f"arr: {mid}")
        
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return False, print(f"Not found")

binarySearch(arr, 9)





"""
"""    