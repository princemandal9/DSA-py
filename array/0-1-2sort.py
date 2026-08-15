def sort(nums):
    i=0
    j=len(nums)-1
    k=0
    while(k<=j):
        if nums[k]==0:
            nums[i],nums[k]=nums[k],nums[i]
            i=i+1
            k=k+1
        elif nums[k]==2:
            nums[j],nums[k]=nums[k],nums[j]
            j=j-1
        else:
            k=k+1
    return nums

a= [1, 1, 2, 2, 1]
print(sort(a))

