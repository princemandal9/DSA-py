#Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
def countsubarr(nums,k):     #bruteforce- nested loop
    count=0
    i=sum=0
    
    while i<len(nums):
        sum=0
        for j in range(i,len(nums)):
            sum+=nums[j]
            if sum==k:
                count+=1
        i+=1
    return count
#TC-N2 SC-1
#def count2(nums,k):

            
nums=[1,2,3]
k=3
print(countsubarr(nums,k))