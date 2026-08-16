#transpose and reverse the matrix
def rotate(a):
    r=len(a)
    row=len(a)
    col=len(a[0])
    for i in range(row):
        for j in range(i+1,col):       #swapping i=j is pointless 
            a[i][j],a[j][i]=a[j][i],a[i][j]
    for i in range(r):
        a[i].reverse()  
    return a

a=[[1,2,3],[4,5,6],[7,8,9]]
print(rotate(a))

#Optimised- use .reverse and swap in transpose
#time-2n^2 , space-1