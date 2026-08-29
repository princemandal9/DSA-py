#merge them without using extra space

#using extra space in array1
def merge(a,b):
    l=0
    k=len(a)-1
    while k>=0 and l<len(b):
        if a[k]>b[l]:
            a[k],b[l]=b[l],a[k]
            l+=1
            k-=1
        else:
            k-=1
    a.sort()
    b.sort()
    for i in range (len(b)):
        a.append(b[i])
    return a
        
#constraint-nums1 has a length of m + n, where the first m elements denote the elements of nums1 and rest are 0s
def merge2(arr1,arr2,m,n):
    #m+n is size of arr1
    i,j,k=m-1,m+n-1,n-1        #three pointer i,j,k
    while k>=0:
        if i>=0 and arr1[i]>arr2[k]:
            arr1[j]=arr1[i]
            j-=1
            i-=1  
        else:
            arr1[j]=arr2[k]
            j-=1
            k-=1
    return arr1
    
nums1 = [-5, -2, 4, 5]
nums2 = [-3, 1, 8]
print(merge(nums1,nums2))
a1=[-5,-2,4,5,0,0,0]
a2=[-3,7,8]
print(merge2(a1,a2,len(a1)-len(a2),len(a2)))