#Find the number that appears once, and the other numbers twice
def singleNumber(nums):
    for i in range(0,len(nums)):
        count=0
        for j in range(0,len(nums)):
            if nums[j]==nums[i]:
                count=count+1
        if count==1:
            return nums[i]   
    return -1

a=[1, 2, 2, 4, 3, 1, 4]
print(singleNumber(a))