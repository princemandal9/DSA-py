def consec(a):
    a.sort()
    count=1
    if(len(a)==1):
        return 1
    maximum=0
    for i in range(1,len(a)):
        if a[i]==a[i-1]+1:
            count+=1
        elif a[i] == a[i-1]:
            continue
        if a[i]!=a[i-1]+1:
            count=0
        maximum=max(maximum,count)
    return maximum

a=[0, 3, 7, 2, 5, 8, 4, 6, 0, 1]  
print(consec(a))