nums = [5,3,7,9]

target = 10

# for i in range(len(nums)):
#     for j in range(i+1, len(nums)):
#         if target == nums[i] + nums[j]:
#             print(nums[i], nums[j], end=" => ")
#             print([i, j])

# print(f"length: {len(nums)}") # -> 4
# print(f"range: {range(0,len(nums), 3)}") # -> 0, 4 i

# for i in range(len(nums)): 
#     print(i, end=", ")

# 
"""
[5,3,7,9]
 ^ ^
 i j
if target = i + j, return i j
if not j +
target = 10


"""
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if target == nums[i] + nums[j]:
                    return [i, j]
                
                
test = Solution()

print(test.twoSum([1,2,3,5,7] ,12))