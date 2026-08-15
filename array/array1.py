def largestElement(nums):
    max=nums[0]
    for i in nums:
        if max<= i:
            max=i
    return max
def secondLargest(nums):
    max1=max(nums[0],nums[1])
    secMax=min(nums[0],nums[1])
    if secMax==max1:
        secMax=float('-inf')
        for i  in nums[2:]:
            if max1<i:   
                secMax=max1
                max1=i
            elif secMax <=i and max1!=i:
                secMax=i
    return secMax if secMax!=float('-inf') else -1
def arrayCheck(nums):   #if sorted or not
    if len(nums)==1:
        return True
    for i in range(0,len(nums)-1): 
        if nums[i] > nums[i+1]:
            return False
    return True
def Duplicate(nums):
     k=0
     for i in range(1, len(nums)):
            if nums[i] != nums[k]:
                k += 1
                nums[k] = nums[i]
     return nums[:k+1] 

a=[1, 1, 1, 2,3,4,5,5]
print(Duplicate(a))