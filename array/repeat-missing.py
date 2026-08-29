#Given an integer array nums of size n containing values from [1, n] ,A-appears twice and B -missing
def repeat_miss(a,n):
    totalSum=n*(n+1)/2
    totalSq=n*(n+1)*(2*n+1)/6
    actualsum=0
    actualsqsum=0

    for i in range(n):
        actualsum+=a[i]
        actualsqsum+=a[i]**2

    diff=totalSum-actualsum                          #y-x
    sqdiff=totalSq-actualsqsum                       #y**2-x**2=(y+x)(y-x)
    sum=sqdiff/diff                                  #y+x= y2-x2/y-x
    missing=(sum+diff)/2                             #y=y+x+y-x/2
    repeating=sum-missing                            #x=sum-missing
    return int(repeating),int(missing)
a=[3,4,5,1,1]
print(repeat_miss(a,len(a)))

#TC=O(N)
