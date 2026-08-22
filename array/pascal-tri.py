#Given two integers r and c, return the value at the rth row and cth column
def pascal1(row,col):
    n=row-1
    r=col-1
    num=den=1
    for i in range(0,r):
        num*=n-i
        den*=i+1
    val=num/den    
    return val

row=int(input("Enter row:"))
col=int(input("Enter col:"))
print(pascal1(row,col))