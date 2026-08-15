#The majority element of an array is an element that appears more than n/2 times in the array.
def majority(nums):    #brute force
    for i in range(len(nums)):
        count=0
        for j in range(len(nums)):
            if nums[j]==nums[i]:
                count=count+1
            if count>len(nums)//2:
                return nums[j]
    return -1

def majority1(nums):   #optimal
    count=1
    for i in range(1,len(nums)):
        temp=nums[0]
        if count==0 :
            temp=nums[i]
            count=count+1
        if temp==nums[i]:
            count=count+1
        if temp!=nums[i]:
            count=count-1
        
    return temp
            


a=[1, 1, 1, 2,2,2, 2]
print(majority(a))

