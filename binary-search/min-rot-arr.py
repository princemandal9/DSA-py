def findMin(nums):
    l=0
    r=len(nums)-1
    ans=nums[0]
    index=0
    if nums[l]<=nums[r]:   #array is sorted
        return nums[l]
    while l<=r:
        mid=l+(r-l)//2
        if nums[l]<=nums[mid]:    #left is sorted
            if nums[l]<ans:         #first elem is minimum in sorted half
                index=l
                ans=nums[l]
            l=mid+1
        else:
            if nums[mid]<ans:         #first elem is minimum in sorted half
                index=mid
                ans=nums[mid]
            r=mid-1
    return [ans,index]    #number of rotation & minimum val

nums=[0,1,2,3,4,5,6]
print(findMin(nums))