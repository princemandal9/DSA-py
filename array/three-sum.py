#triplets summing upto zero
s=set()
def threesum(nums):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            for k in range(j+1,len(nums)):
                if nums[i]+nums[j]+nums[k]==0:
                    triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
    s.add(triplet)
    return s
#tc: n3   and sc: no.of triplets

#optimised-two pointers
def threeSum2(a):
    a=sorted(a)
    i=0
    res=[]
    for i in range(len(a)-2):   #we want to trverse till third last elem for triplet
        if i > 0 and a[i] == a[i - 1]:
            continue
        j=i+1
        k=len(a)-1
        while j<k:
            if a[i]+a[j]+a[k]==0:
                res.append((a[i],a[j],a[k]))
                k-=1
                j+=1
                while j<k and a[j-1]==a[j]:    #avoiding identical triplets
                    j+=1
                while j<k and a[k+1]==a[k]:
                    k-=1
            elif a[i]+a[j]+a[k]>0:
                k-=1
            else:
                j+=1
    return res
        
a=[2, -2, 0, 3, -3, 5]
print(threeSum2(a))