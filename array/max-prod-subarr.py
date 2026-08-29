# Find the subarray with the largest product, and return the product of the elements present in that subarray.
#brute force- nested loop, storing maxproduct- TC:O(n2)
#optimal- two pointers
def max_prod(a):
    prefix,suffix=1,1
    maximum=0
    i=0
    j=i
    k=len(a)-1
    for i in range(len(a)):
        if prefix==0:         #Reset the product to 1 whenever a zero is found
            prefix=1
        if suffix==0:
            suffix=1

        prefix*=a[j]
        suffix*=a[k]
        #By comparing products in both directions, we ensure we don’t miss any possible maximum.
        maximum=max(maximum,prefix,suffix)
        k=k-1
    return maximum
a=[1,2,-3,-2,0,-5]
print(max_prod(a))
        
        