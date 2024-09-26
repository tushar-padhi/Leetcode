l1 = [6,4,5,0]
l2 = [4,5,0,0,0]

set1 = set(l1)
set2 = set(l2)

r1 = list(set1 - set2)
r2 = list(set2 - set1)

result = [r1,r2]

print(result)