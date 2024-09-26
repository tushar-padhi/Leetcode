def jump_game_2(nums):
    
    #nums = [2,3,1,1,4]
    n = len(nums)

    j = 0
    for i in range(n):
        if i + nums[i] != nums[n-1]:
            j += 1
        else:
            return i+j
            
nums_1 = [2,3,4]    
print(jump_game_2(nums_1))