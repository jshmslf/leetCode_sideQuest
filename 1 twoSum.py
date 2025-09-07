nums = [5,3,7,9]

target = 10

for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if target == nums[i] + nums[j]:
            print([i, j])