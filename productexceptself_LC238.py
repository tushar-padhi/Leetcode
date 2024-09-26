
import math

def productexceptself(nums):
    
    answer = []
    test = {}
    for i in range(len(nums)):   
        rotated_list = nums[i+1:] + nums[:i]
        test[nums[i]] = rotated_list
    return test
    #temp = 1
    for key in test:
        temp = math.prod(test[key])
        answer.append(temp)
        
    return answer
    

nums = [1,1]
print(productexceptself(nums))

#nums.remove(1)
#print(nums)


    