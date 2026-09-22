def singleNonDuplicate( nums):
     l=0
     r=len(nums)-1
     while l<=r:
        mid=l+(r-l)//2
        if mid%2==0:     #mid is even
            mid=mid-1
        #we will have mid in odd position
        if nums[mid]==nums[mid-1]:     #no break in pattern,no single elem in this half
            l=mid+2
        else:
            r=mid-1
     return nums[r]

nums=[1,1,2,2,3,3,4,5,5,6,6]
print(singleNonDuplicate(nums))