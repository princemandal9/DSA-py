#union of two sorted arrays
def union(nums1,nums2):   #Brute force approach
    uni={}
    for i in nums1:
        uni[i]=True
    for j in nums2:
        uni[j]=True
    result=list(uni.keys())
    result.sort()
    return result

def union2(nums1,nums2):   #Optimal
    uni=[]
    i=0
    j=0
    k=0
    while i<len(nums1) and j<len(nums2):
        if i > 0 and nums1[i] == nums1[i-1]:
             i += 1
             continue
                # skip duplicates within nums2
        if j > 0 and nums2[j] == nums2[j-1]:
             j += 1
             continue
        if nums1[i]<nums2[j]:
            uni.append(nums1[i])
            i=i+1
            k=k+1
        elif nums1[i]==nums2[j]:
            uni.append(nums1[i])
            i=i+1
            j=j+1
            k=k+1
        else:
            uni.append(nums2[j])
            k=k+1
            j=j+1
    while i<len(nums1):
        uni.append(nums1[i])
        k=k+1
        i=i+1
    while j<len(nums2):
        uni.append(nums2[j])
        k=k+1
        j=j+1
    return uni

    
a=[3,3,3,4,5,6,8]
b=[1,4,6,55,100]
print(union2(a,b))
