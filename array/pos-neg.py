a=[2,3,-2,4,-5,-6]
arr=[0]*len(a)          #declaring array of size of a
positive=0
negative=1


for i in range(0,len(arr)):
    if a[i]>0:
        arr[positive]=a[i]
        positive+=2
    if a[i]<0:
        arr[negative]=a[i]
        negative+=2
print(arr)