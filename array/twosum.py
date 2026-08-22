#return the index number of two element whose sum =target
def twoSum(nums,k):   #brute force
    for i in range(len(nums)):
        Sum=0
        for j in range(len(nums)):
            sum=nums[i]+nums[j]
            if sum==k:
                return i,j
    return -1


def twoSum1(nums,k):  #optimised solution 
    nums=sorted(nums)
    i=0
    j=len(nums)-1
    while(i<=len(nums)):
        if nums[i]+nums[j]<k:
            i=i+1
        else:
            j=j-1
        if nums[i]+nums[j]==k:
            return [i,j]
    return [-1,-1]


a=[-6, 7, 1, -7, 6, 2,1]
n=3
print(twoSum(a,n))

#time complexity-nlogn+n
#space complexity-1