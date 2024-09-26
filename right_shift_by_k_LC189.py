nums1 = [1,2,3,4,5,6,7]
k = 3

n = len(nums1)

# popped_no = []

# if k <=2:
    
#     for i in range(len(nums1)-1,k-1,-1):
#         popped_no.append(nums1.pop(i))
#     print(popped_no[::-1])
# else:
#     for i in range(len(nums1)-1,k,-1):
#         popped_no.append(nums1.pop(i))
#     print(popped_no[::-1])
# nums1 = popped_no[::-1] + nums1
# print(nums1)
# #print(nums1[i])

def reverse(start,end):
    while start < end:
        nums1[start] , nums1[end] = nums1[end], nums1[start]
        start += 1
        end -= 1
reverse(0, n-1)
print(nums1)
reverse(0,k-1)
print(nums1)
reverse(k, n-1)
print(nums1)

