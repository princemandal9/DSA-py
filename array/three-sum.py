#triplets summing upto zero
s=set()
def threesum(nums):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            for k in range(j+1,len(nums)):
                if nums[i]+nums[j]+nums[k]==0:
                    triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
    s.add(triplet)
    return s
a=[2, -1, -1, 3, -1]
print(threesum(a))