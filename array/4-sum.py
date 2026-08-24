def foursum(a,target):
    a=sorted(a)
    i=0
    res=[]
    for i in range(len(a)-3):   #we want to trverse till third last elem for triplet
        if i > 0 and a[i] == a[i - 1]:
            continue
        for j in range(i+1,len(a)-2):
            if a[j] == a[j - 1]:
                continue
            k=j+1
            l=len(a)-1
            while k<l:
                if a[i]+a[j]+a[k]+a[l]==target:
                    res.append((a[i],a[j],a[k],a[l]))
                    l-=1
                    k+=1
                    while k<l and a[k-1]==a[k]:    #avoiding identical triplets
                        k+=1
                    while k<l and a[l+1]==a[l]:  #keep decreasing until we get diff value
                        l-=1
                elif a[i]+a[j]+a[k]+a[l]>target:
                    l-=1
                else:
                    k+=1
    return res
        
a= [1, -2, 3, 5, 7, 9]
target=7
print(foursum(a,target))