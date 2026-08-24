def largestSub(a):
    sum=0
    max_sub=0
    for i in range(len(a)):
        sum=a[i]
        for j in range(i+1,len(a)):
            sum+=a[j]
            if sum==0:          #need to save the length of the subarray, j-i+1 gives the size of subarr
                max_sub=max(max_sub,j-i+1)  
    return max_sub     
#bruteforce- tc: o(n2)

a=[9, -3, 3, -1, 6, -5]
print(largestSub(a))