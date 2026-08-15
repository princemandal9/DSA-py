def maxConsec(nums):  #maximum consecutive 1s
    count=1
    maxCount=-1
    for i in range(0,len(nums)):
        if nums[i]==1:
            count=count+1
        else:
            count=0
        maxCount=max(maxCount,count)
    return maxCount

a= [1, 0, 1, 1, 1, 0, 1, 1, 1]
print(maxConsec(a))