def mostFrequentElement(nums):
        freq={}
        maxFreq=0
        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        maxFreq=max(freq.values())
        ans=float('inf')
        for j in freq:
             if freq[j]==maxFreq and j<ans:
                  ans=j
        return ans

def selectionSort(nums):
        temp=0
        for i in range(0,len(nums)):
            minIndex=i
            for j in range(i+1,len(nums)):
                if nums[j]<nums[minIndex]:
                     minIndex=j
            temp = nums[i]
            nums[i] = nums[minIndex]
            nums[minIndex] = temp                     
                    
        return nums

#merge sort
class Solution:
    def mergeSort(self, nums):
        startIndex=0
        endIndex=len(nums)-1
        self.divide(nums,startIndex,endIndex)
        return nums
    def divide(self, arr, startIndex, endIndex):
        if(startIndex<endIndex):
            mid= startIndex + (endIndex-startIndex)//2
            self.divide(arr, startIndex,mid )
            self.divide(arr, mid+1, endIndex)
            self.merge(arr,startIndex,mid,endIndex)
    def merge(self,arr,startIndex,mid,endIndex):
        i=startIndex
        j=mid+1
        temp=[]
        while(i<=mid and j<=endIndex):
            if(arr[i]<=arr[j]):
                temp.append(arr[i])
                i+=1
            else:
                temp.append(arr[j])
                j+=1
        while(i<=mid):
                temp.append(arr[i])
                i+=1
        while(j<=endIndex):
                temp.append(arr[j])
                j+=1
        for k in range(0,len(temp)):
                arr[startIndex+k]=temp[k]
""" a=[7,3,2,8,5,2,1,9]
sol = Solution()
nums = [7, 4, 1, 5, 3]
print(sol.mergeSort(nums)) """

#bubble sort
def bubbleSort(arr):
     temp=0
     for i in range(0,len(arr)):
          for j in range(0,len(arr)-i-1):
               if arr[j]>=arr[j+1]:
                    temp=arr[j]
                    arr[j]=arr[j+1]
                    arr[j+1]=temp
     return arr


a=[9,3,13,5,2,7,1]
print(bubbleSort(a))
            