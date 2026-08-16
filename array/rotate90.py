#transpose and reverse the matrix
def rotate(a):
    a=transpose(a)
    r=len(a)
    #reverse- can be done using .reverse 
    for i in range(r):
        a[i].reverse()      #reverse each row one by one
    return a

def transpose(a):
    row=len(a)
    col=len(a[0])
    for i in range(row):
        for j in range(i+1,col):       #swapping i=j is pointless ..a[0][0] so we used j=i+1 to avoid swapping diagonal elem.
            a[i][j],a[j][i]=a[j][i],a[i][j]
    return a

a=[[1,2,3],[4,5,6],[7,8,9]]
print(rotate(a))

#Optimised- use .reverse and swap in transpose
#time-2n^2 , space-1