#SLIDING WINDOW PATTERN
#method_1 #set

# def lengthOfLongestSubstring(s):
#     left = max_length = 0
#     char_set = set()
    
#     for right in range(len(s)):
#         while s[right] in char_set:
#             char_set.remove(s[left])  
#             left += 1
#         char_set.add(s[right])  
#         max_length = max(max_length, right - left + 1)
#     return max_length

# s = "abcabcbb"
# print(lengthOfLongestSubstring(s))

#method_2 #hash map
def lengthOfLongestSubstring(s):
    left = max_length = 0
    count = {}
    
    for right, c in enumerate(s):
        count[c] = 1 + count.get(c, 0)
        while count[c] > 1:
            count[s[left]] -= 1
            left += 1
        
        max_length = max(max_length, right - left + 1)
        
    return max_length
 
s = "abcabcbb"
print(lengthOfLongestSubstring(s))


    