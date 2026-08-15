#Kadanes algo- max subarray
#brute force
def kadane(nums):
    max_count=float('-inf')
    for i in range(len(nums)):
        for j in range(i,len(nums)):
            count=0
            
            for k in range(i,j+1):
                count+=nums[k]
                max_count=max(count,max_count)
    return max_count
#optimised
def kadane1(nums):
    i=0
    sum=0
    maxsum=float('-inf')
    for i in range(len(nums)):
        sum+=nums[i]
        maxsum=max(sum,maxsum)
        if sum<0:
            sum=0
    return maxsum

a=[-2, -3, -7, -2, -10, -4]
print(kadane(a))