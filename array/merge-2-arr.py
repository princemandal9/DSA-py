def merge(a,b):
    l=0
    k=len(a)-1
    merge_arr= []
    while k>0 and l<len(b):
        if a[k]>b[l]:
            a[k],b[l]=b[l],a[k]
            l+=1
            k-=1
        else:
            k-=1
    a.sort()
    b.sort()
    # Add elements from first array
    for i in range (len(a)):
        merge_arr.append(a[i])
    for i in range (len(b)):
        merge_arr.append(b[i])
    return merge_arr
        

nums1 = [-5, -2, 4, 5]
nums2 = [-3, 1, 8]
print(merge(nums1,nums2))
