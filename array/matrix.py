def addition(a,b):
    row=len(a)              #counting number of lists in list= row
    column=len(a[0])          #counts number of element in list within list=col
    add=[[0]*column for x in range(row)]         #declaring a matrix
    for i in range(row):
        for j in range(column):
            add[i][j]=a[i][j]+b[i][j]
    return add

def multiply(a,b):
    row=len(a)              
    column=len(a[0])          
    mul=[[0]*column for x in range(row)] 
    for i in range(row):
        for j in range(row):
            mul[i][j]=0
            for k in range(column):
                mul[i][j]+=a[i][k]*b[k][j]
    return mul

def transpose(a):
    r=len(a)
    c=len(a[0])
    t=[[0]*r for i in range(c)]       #transpose matrix order is reversed
    for i in range(r):
        for j in range(c):
            t[j][i]=a[i][j]
    return t

rows=3
cols=3
b=[[2,1,2],[3,2,1],[1,1,1]]
a=[[2], [3], [1]]
print(a)
print(b)
#print(addition(a,b))
#print(multiply(a,b))
print(transpose(a))

