class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if target == nums[mid]:
                return mid
            
            if target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1

        return l



z = Solution()
y = z.searchInsert([1,3,5,6] ,7)


print(y)

"""
target = 5
[1, 3, 5, 6]
 l  m     r



"""