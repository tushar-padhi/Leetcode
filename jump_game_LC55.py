def jump_game(nums):

    max = len(nums) - 1
    for i in range(len(nums)-2, -1,-1):
        if i + nums[i] >=max:
            max = i
    if max== 0:
        return True
    else:
        return False 
nums = [2,3,1,0,4]
print(jump_game(nums))

