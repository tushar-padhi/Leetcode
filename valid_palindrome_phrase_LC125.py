# import re

# s = "race a car"

# new_str = re.sub(r'[^a-zA-Z0-9]', "", s).lower()

# print(new_str)

# if new_str == new_str[::-1]:
#     print(True)
# else:
#     print(False)

#method 1
s = "A man, a plan, a canal: Panama"

new_str = []
for char in s:
    if char.isalnum():
        new_str.append(char.lower())
print("".join(new_str))

#method 2 use two pointer technique

l = 0
r = len(s) - 1
while l < r:
    if not s[l].isalnum():
        l += 1
    elif not s[r].isalnum():
        r -= 1
    elif s[l].lower() == s[r].lower():
        l +=1
        r -=1
    else:
        print(False)
print(True)
    




        
