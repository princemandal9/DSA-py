def moveZeros(arr):      #BRUTE FORCE
    dup=[]
    for i in range(0,len(arr)):
        if arr[i]!=0:
            dup.append(arr[i])
    for x in range(0,len(dup)):
        arr[x]=dup[x]
    for y in range(0,len(arr)-len(dup)):
        arr[len(dup)+y]=0
    return arr
def movezero(arr):
    k=0
    i=0
    while i< len(arr)-k:
        if arr[i]==0:
            arr[i],arr[len(arr)-1-k]= arr[len(arr)-1-k],arr[i]
            k=k+1
        else:
            i=i+1
    return arr

a=[1,2,0,1,0,3]
print(movezero(a))