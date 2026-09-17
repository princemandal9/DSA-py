#lowerbound
def lowerBound(nums,x):
    left=0
    right=len(nums)-1
    result=len(nums)
    while left<=right:
        mid=left+(right-left)//2
        if nums[mid]>=x:
            result=mid
            right=mid-1
        else:
            left=mid+1
    return result

nums=[3,5,8,15,19]
x=9
print(lowerBound(nums,x))   
