#Given an array nums of size n and an integer k, find the length of the longest sub-array that sums to k
def longest(nums,k):
    longest_arr=0
    for i in range(len(nums)):
        subarray_sum=0
        for j in range(i,len(nums)):
            subarray_sum=subarray_sum+nums[j]
            if subarray_sum==k:
                longest_arr=max(longest_arr,j-i+1)
    return longest_arr

a= [-1,1,1]
k=1
print(longest(a,k))
