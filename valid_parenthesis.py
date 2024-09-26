
def twoSum(nums=[], target=6):
    pointer_1 = 0
    pointer_2 = len(nums) - 1
    while pointer_1 < pointer_2:
        sum = nums[pointer_1] + nums[pointer_2]
        if sum == target:
            return [pointer_1, pointer_2]
        elif sum < target:
            pointer_1 += 1
        else:
            pointer_2 -= 1
    return []

nums = [2,3,4]
print(twoSum(nums))