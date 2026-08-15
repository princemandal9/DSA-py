#A leader in an array is an element whose value is strictly greater than all elements to its right in the given array.
#Input: nums = [1, 2, 5, 3, 1, 2]    Output: [5, 3, 2]
def leaders(a):
    b=[]
    b.append(a[-1])
    k=0
    for i in range(len(a)-1,-1,-1):
        if a[i]>b[k]:
            b.append(a[i])
            k+=1
    b.reverse()
    return b

a= [-3, 4, 5, 1, -4, -5]
print(leaders(a))

#We iterate from right to left we know leaders will always be greater thwn right side elements