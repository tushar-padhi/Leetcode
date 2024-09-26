t = 'baab'
s = 'ab'

p1 = ''
for char in range(len(t)):
    if t[char] in s:
        p1 = p1 + char
print(p1)
# if p1 == s:
#     #print(True)
# else:
#     #print(False)