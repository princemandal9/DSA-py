#Input: Arr[] = {1,3,2}   Output: {2,1,3}
a=[2,1,5,4,4,3,0]
print(next(a))
#breakeven point
def next(a):
    break_=-1
    for i in range(len(a)-1,0,-1):
        if a[i]>a[i-1]:
            break_=i-1
            break
    if break_==-1:
        a.reverse()
        return
#smallest larger number to the right side of breakpoint
    maxim=a[break_+1] 
    larg=break_+1 
    for j in range(break_+1,len(a)):     
        if a[j]>a[break_]:
            maxim=min(maxim,a[j])    #smallest larger number than 1
            larg=j

#swapping the larger value with breakeven point
    a[break_],a[larg]=a[larg],a[break_]
    a[break_+1:]=sorted(a[break_+1:])
    return 
