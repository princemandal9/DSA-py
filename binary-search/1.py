#Search X in sorted array
def search(nums,target):
    left=0
    right=len(nums)-1
    while left<=right:
        mid=left+(right-left)//2
        if target>nums[mid]:
            left=mid+1
        elif target<nums[mid]:
            right=mid-1
        else:
            return mid
    return -1

nums=[-3,-1,-1,0,3,5,9,12]
target=0
print(search(nums,target))

#TC=O(LOGN)