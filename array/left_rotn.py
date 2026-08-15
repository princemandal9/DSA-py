def rotate_left(arr):
    dup = arr[0]
    if len(arr)<=1:
        return arr
    for i in range(1,len(arr)):
        arr[i-1] = arr[i]
    arr[-1] = dup  #last element shifted
    return arr
def rotatebyK(arr,k):   #Brute force
    temp={}
    for i in range(0,k):
        temp[i]=arr[i]
    for j in range(k,len(arr)):
        arr[j-k]=arr[j]
    n=0
    p=len(arr)-k
    while(p<len(arr)):
        arr[p]=temp[n]
        n=n+1
        p=p+1
    return arr
def reverse(arr,x,y):
    i=x
    j=y-1
    while(i<j):
        arr[j],arr[i]=arr[i],arr[j]
        i=i+1
        j=j-1
    return arr
def rotate(arr,k,n):
    reverse(arr,0,k)
    reverse(arr,k,n)
    reverse(arr,0,n)
    return arr
a = [1,2,3,4]
n=len(a)
number=int(input('Enter the rotation no: '))
k=number%len(a)
#print(rotatebyK(a,k))
print(rotate(a,k,n))
