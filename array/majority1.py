#The majority element of an array is an element that appears more than n/2 times in the array.
def majority(nums):    #brute force
    for i in range(len(nums)):
        count=0
        for j in range(len(nums)):
            if nums[j]==nums[i]:
                count=count+1
            if count>len(nums)//2:
                return nums[j]
    return -1

def majority1(nums):   #optimal
    count=1
    for i in range(1,len(nums)):
        temp=nums[0]
        if count==0 :
            temp=nums[i]
            count=count+1
        if temp==nums[i]:
            count=count+1
        if temp!=nums[i]:
            count=count-1
    return temp


#Return all elements which appear more than n/3 times in the array
def majority2(nums):
    count1=count2=0
    elem1=elem2=0
    #maximum 2 majority elements possible so getting them first
    for i in range(len(nums)):
        if count1==0 and elem2!=nums[i]:
            elem1=nums[i]
            count1+=1
        elif count2==0 and elem1!=nums[i]:
            elem2=nums[i]
            count2+=1
        elif elem1==nums[i]:
            count1+=1
        elif elem2==nums[i]:
            count2+=1
        else:
            count1-=1
            count2-=1
    #Now seeing which one has more than n//3 elem
    c1=c2=0
    result=[]
    for j in nums:
        if j==elem1:
            c1+=1
        elif j==elem2:
            c2+=1
    m=len(nums)//3        #
    if c1>m:
        result.append(elem1)
    if c2>m:
        result.append(elem2)
    return result

a=[1, 2, 1, 1, 3, 2]
print(majority2(a))
#TC: n+n SC: 1

