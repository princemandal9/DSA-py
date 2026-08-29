#need to return the count of reverse pairs. Reverse Pairs are those pairs where i<j and arr[i]>2*arr[j].
def reversePair(a):                           #TC=O(n2)
    count=0
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[i]> 2*a[j]:
                count+=1
    return count
#constraint= 2^31 <= nums[i] <= 2^31 - 1 

def reversePair2(a):
    


a=[1,3,2,3,1]
print(reversePair(a))