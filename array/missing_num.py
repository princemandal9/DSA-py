def missing(a):
    n=len(a)
    sum=n*(n+1)//2
    currSum=0
    for i in range(0,len(a)):
        currSum=a[i]+currSum
    return sum-currSum

nums=[0, 1, 2, 4, 5, 6]
print(missing(nums))