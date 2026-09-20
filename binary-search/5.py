#floor and ceiling
def getFloorAndCeil( nums, x):
    left=0
    right=len(nums)-1
    floor,ceil=-1,-1
    while left<=right:
        mid=left+(right-left)//2
        if nums[mid]==x:
            return x,x
        elif nums[mid]<x:
            left=mid+1
            ceil=mid
        else:
            right=mid-1
            floor=mid
    return [ceil,floor]
nums=[1,3,4,5,9]
x=6
print(getFloorAndCeil(nums,x))