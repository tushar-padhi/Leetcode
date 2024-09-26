a = 'abcd'
print(map(a.upper(),a))
b = list(map(lambda x:x.upper(), a))

print(lambda x:x.upper(), a)

print(b)


c = {2,3,5}

print(c.pop())